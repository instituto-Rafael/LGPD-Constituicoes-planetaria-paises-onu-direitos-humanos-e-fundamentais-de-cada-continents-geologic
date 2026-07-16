#!/usr/bin/env python3
"""Finite eight-heuristic aviation audit ruler.

This tool performs deterministic screening only. It does not determine
causation, legal liability, insurance coverage, airworthiness, or fraud.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

HEURISTIC_IDS = tuple(f"H{i}" for i in range(1, 9))
BANDS = (
    (20.0, "MONITOR"),
    (40.0, "REVIEW"),
    (60.0, "TARGETED_AUDIT"),
    (80.0, "URGENT_AUDIT"),
    (101.0, "CRITICAL"),
)


class InputError(ValueError):
    """Raised when the input contract is invalid."""


def _number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise InputError(f"{field} must be numeric")
    return float(value)


def _band(score: float) -> str:
    for threshold, label in BANDS:
        if score < threshold:
            return label
    return "CRITICAL"


def _canonical_hash(data: dict[str, Any]) -> str:
    payload = json.dumps(
        data, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def evaluate(data: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(data, dict):
        raise InputError("root must be an object")

    case_id = data.get("case_id")
    if not isinstance(case_id, str) or not case_id.strip():
        raise InputError("case_id must be a non-empty string")

    heuristics = data.get("heuristics")
    if not isinstance(heuristics, dict):
        raise InputError("heuristics must be an object")

    missing = [hid for hid in HEURISTIC_IDS if hid not in heuristics]
    extra = sorted(set(heuristics) - set(HEURISTIC_IDS))
    if missing:
        raise InputError(f"missing heuristics: {', '.join(missing)}")
    if extra:
        raise InputError(f"unknown heuristics: {', '.join(extra)}")

    weighted_known = 0.0
    weighted_known_capacity = 0.0
    weighted_total_capacity = 0.0
    weighted_evidence = 0.0
    unknown_weight = 0.0
    normalized: dict[str, Any] = {}

    for hid in HEURISTIC_IDS:
        item = heuristics[hid]
        if not isinstance(item, dict):
            raise InputError(f"heuristics.{hid} must be an object")

        weight = _number(item.get("weight", 1.0), f"heuristics.{hid}.weight")
        evidence = _number(item.get("evidence", 0.0), f"heuristics.{hid}.evidence")
        score = item.get("score")
        state = item.get("state", "TOKEN_VAZIO" if score is None else "ASSESSED")

        if weight <= 0:
            raise InputError(f"heuristics.{hid}.weight must be > 0")
        if not 0.0 <= evidence <= 1.0:
            raise InputError(f"heuristics.{hid}.evidence must be between 0 and 1")
        if score is not None:
            if isinstance(score, bool) or not isinstance(score, int):
                raise InputError(f"heuristics.{hid}.score must be integer 0..4 or null")
            if not 0 <= score <= 4:
                raise InputError(f"heuristics.{hid}.score must be integer 0..4 or null")
        elif evidence != 0.0:
            raise InputError(
                f"heuristics.{hid}.evidence must be 0 when score is null"
            )

        weighted_total_capacity += 4.0 * weight
        weighted_evidence += weight * evidence

        if score is None:
            unknown_weight += weight
        else:
            weighted_known += weight * score
            weighted_known_capacity += 4.0 * weight

        normalized[hid] = {
            "score": score,
            "weight": round(weight, 6),
            "evidence": round(evidence, 6),
            "state": str(state),
            "notes": str(item.get("notes", "")),
            "source_refs": item.get("source_refs", []),
        }

    total_weight = weighted_total_capacity / 4.0
    coverage = 100.0 * weighted_evidence / total_weight
    lower = 100.0 * weighted_known / weighted_total_capacity
    upper = 100.0 * (
        weighted_known + 4.0 * unknown_weight
    ) / weighted_total_capacity
    observed = (
        100.0 * weighted_known / weighted_known_capacity
        if weighted_known_capacity > 0
        else None
    )

    hard_gates = data.get("hard_gates", {})
    if not isinstance(hard_gates, dict):
        raise InputError("hard_gates must be an object")

    triggered: list[str] = []
    for gate, value in sorted(hard_gates.items()):
        if not isinstance(gate, str) or not isinstance(value, bool):
            raise InputError("hard_gates must map strings to booleans")
        if value:
            triggered.append(gate)

    if triggered:
        decision = "BLOCKED_REVIEW_REQUIRED"
    elif coverage < 60.0:
        decision = "INSUFFICIENT_EVIDENCE"
    elif observed is None:
        decision = "INSUFFICIENT_EVIDENCE"
    else:
        decision = _band(observed)

    result = {
        "schema_version": "aviation-audit-ruler-8h/v1",
        "case_id": case_id,
        "screening_only": True,
        "causal_claim_allowed": False,
        "input_sha256": _canonical_hash(data),
        "heuristics": normalized,
        "risk": {
            "observed_score_0_100": None if observed is None else round(observed, 3),
            "lower_bound_0_100": round(lower, 3),
            "upper_bound_0_100": round(upper, 3),
            "evidence_coverage_0_100": round(coverage, 3),
            "observed_band": None if observed is None else _band(observed),
        },
        "hard_gates_triggered": triggered,
        "decision": decision,
        "epistemic_note": (
            "The ruler prioritizes audit work. It does not prove pilot error, "
            "operator fault, maintenance error, insurance coverage, or fraud."
        ),
    }
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="input JSON file")
    parser.add_argument("-o", "--output", type=Path, help="output JSON file")
    args = parser.parse_args(argv)

    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        result = evaluate(data)
    except (OSError, json.JSONDecodeError, InputError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
