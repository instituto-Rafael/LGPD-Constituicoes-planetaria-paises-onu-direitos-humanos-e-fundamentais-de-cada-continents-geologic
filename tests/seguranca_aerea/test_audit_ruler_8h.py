#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "scripts" / "seguranca_aerea" / "audit_ruler_8h.py"
SPEC = importlib.util.spec_from_file_location("audit_ruler_8h", MODULE_PATH)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


def base_case():
    return {
        "case_id": "TEST",
        "heuristics": {
            f"H{i}": {
                "score": None,
                "weight": 1,
                "evidence": 0,
                "state": "TOKEN_VAZIO",
                "notes": "",
                "source_refs": [],
            }
            for i in range(1, 9)
        },
        "hard_gates": {},
    }


class AuditRulerTests(unittest.TestCase):
    def test_all_unknown_preserves_uncertainty(self):
        result = audit.evaluate(base_case())
        self.assertEqual(result["decision"], "INSUFFICIENT_EVIDENCE")
        self.assertEqual(result["risk"]["lower_bound_0_100"], 0.0)
        self.assertEqual(result["risk"]["upper_bound_0_100"], 100.0)
        self.assertFalse(result["causal_claim_allowed"])

    def test_complete_assessment(self):
        case = base_case()
        for item in case["heuristics"].values():
            item.update(score=2, evidence=1, state="ASSESSED")
        result = audit.evaluate(case)
        self.assertEqual(result["risk"]["observed_score_0_100"], 50.0)
        self.assertEqual(result["risk"]["evidence_coverage_0_100"], 100.0)
        self.assertEqual(result["decision"], "TARGETED_AUDIT")

    def test_hard_gate_overrides_score(self):
        case = base_case()
        for item in case["heuristics"].values():
            item.update(score=0, evidence=1, state="VERIFIED")
        case["hard_gates"]["component_life_limit_exceeded"] = True
        result = audit.evaluate(case)
        self.assertEqual(result["decision"], "BLOCKED_REVIEW_REQUIRED")
        self.assertEqual(
            result["hard_gates_triggered"], ["component_life_limit_exceeded"]
        )

    def test_rejects_nonzero_evidence_for_unknown_score(self):
        case = base_case()
        case["heuristics"]["H1"]["evidence"] = 0.5
        with self.assertRaises(audit.InputError):
            audit.evaluate(case)


if __name__ == "__main__":
    unittest.main()
