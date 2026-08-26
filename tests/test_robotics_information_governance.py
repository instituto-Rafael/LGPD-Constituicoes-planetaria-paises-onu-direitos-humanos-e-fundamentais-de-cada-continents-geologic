import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "robotics_information_governance_v1.json"


def load_registry():
    with REGISTRY.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def test_registry_has_seven_layers_with_seven_questions_each():
    registry = load_registry()
    assert len(registry["layers"]) == 7
    assert [layer["id"] for layer in registry["layers"]] == [f"L{i}" for i in range(1, 8)]
    for layer in registry["layers"]:
        assert len(layer["questions"]) == 7
        assert all(isinstance(question, str) and question.strip() for question in layer["questions"])


def test_first_question_gate_does_not_conflate_notice_and_consent():
    gate = load_registry()["first_question_gate"]
    assert gate["required_by_this_framework"] is True
    assert gate["claimed_as_general_lgpd_literal_requirement"] is False
    assert "ACKNOWLEDGED != OPTIONAL_CONSENT_GRANTED" in gate["invariants"]
    assert "information != consent" in gate["invariants"]
    assert "consent_is_not_the_only_legal_basis" in gate["invariants"]


def test_robotics_is_not_misrepresented_as_a_legal_term():
    term = load_registry()["term"]
    assert term["name"] == "Robotics"
    assert term["legal_term"] is False
    assert term["legal_role_override_forbidden"] is True


def test_unknown_claims_remain_token_vazio():
    gates = load_registry()["evidence_gates"]
    assert gates["G3_fqg_required_by_law"] == "TOKEN_VAZIO"
    assert gates["G4_robotics_is_legal_term"] == "TOKEN_VAZIO"
    assert gates["G5_product_implementation"] == "TOKEN_VAZIO"
    assert gates["G6_independent_usability_test"] == "TOKEN_VAZIO"
    assert gates["G7_market_power_claims"] == "TOKEN_VAZIO"


def test_serious_claims_require_evidence_state_machine():
    policy = load_registry()["serious_claim_policy"]
    required_terms = {"monopoly", "oligopoly", "cartel", "collusion", "criminal_organization", "mafia"}
    assert required_terms.issubset(set(policy["terms_requiring_evidence"]))
    assert policy["states"][0] == "OBSERVACAO"
    assert "TOKEN_VAZIO" in policy["states"]
    assert len(policy["market_concentration_minimum_fields"]) >= 6


def test_all_analytical_transforms_are_marked_non_proof():
    transforms = load_registry()["analytical_transforms"]
    assert transforms
    assert all(transform["legal_proof"] is False for transform in transforms)


def test_official_sources_are_https_and_date_stamped():
    sources = load_registry()["official_sources"]
    assert len(sources) >= 3
    for source in sources:
        assert source["url"].startswith("https://")
        assert source["checked_at"] == "2026-08-26"
