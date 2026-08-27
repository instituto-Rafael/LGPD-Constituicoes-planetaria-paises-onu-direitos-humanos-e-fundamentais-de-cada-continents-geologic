import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "robotics_information_governance_v1.json"


def load_registry():
    with REGISTRY.open("r", encoding="utf-8") as handle:
        return json.load(handle)


class RoboticsInformationGovernanceTests(unittest.TestCase):
    def test_registry_has_seven_layers_with_seven_questions_each(self):
        registry = load_registry()
        self.assertEqual(len(registry["layers"]), 7)
        self.assertEqual([layer["id"] for layer in registry["layers"]], [f"L{i}" for i in range(1, 8)])
        for layer in registry["layers"]:
            self.assertEqual(len(layer["questions"]), 7)
            self.assertTrue(all(isinstance(question, str) and question.strip() for question in layer["questions"]))

    def test_first_question_gate_does_not_conflate_notice_and_consent(self):
        gate = load_registry()["first_question_gate"]
        self.assertIs(gate["required_by_this_framework"], True)
        self.assertIs(gate["claimed_as_general_lgpd_literal_requirement"], False)
        self.assertIn("ACKNOWLEDGED != OPTIONAL_CONSENT_GRANTED", gate["invariants"])
        self.assertIn("information != consent", gate["invariants"])
        self.assertIn("consent_is_not_the_only_legal_basis", gate["invariants"])

    def test_robotics_is_not_misrepresented_as_a_legal_term(self):
        term = load_registry()["term"]
        self.assertEqual(term["name"], "Robotics")
        self.assertIs(term["legal_term"], False)
        self.assertIs(term["legal_role_override_forbidden"], True)

    def test_unknown_claims_remain_token_vazio(self):
        gates = load_registry()["evidence_gates"]
        self.assertEqual(gates["G3_fqg_required_by_law"], "TOKEN_VAZIO")
        self.assertEqual(gates["G4_robotics_is_legal_term"], "TOKEN_VAZIO")
        self.assertEqual(gates["G5_product_implementation"], "TOKEN_VAZIO")
        self.assertEqual(gates["G6_independent_usability_test"], "TOKEN_VAZIO")
        self.assertEqual(gates["G7_market_power_claims"], "TOKEN_VAZIO")

    def test_serious_claims_require_evidence_state_machine(self):
        policy = load_registry()["serious_claim_policy"]
        required_terms = {"monopoly", "oligopoly", "cartel", "collusion", "criminal_organization", "mafia"}
        self.assertTrue(required_terms.issubset(set(policy["terms_requiring_evidence"])))
        self.assertEqual(policy["states"][0], "OBSERVACAO")
        self.assertIn("TOKEN_VAZIO", policy["states"])
        self.assertGreaterEqual(len(policy["market_concentration_minimum_fields"]), 6)

    def test_all_analytical_transforms_are_marked_non_proof(self):
        transforms = load_registry()["analytical_transforms"]
        self.assertTrue(transforms)
        self.assertTrue(all(transform["legal_proof"] is False for transform in transforms))

    def test_official_sources_are_https_and_date_stamped(self):
        sources = load_registry()["official_sources"]
        self.assertGreaterEqual(len(sources), 3)
        for source in sources:
            self.assertTrue(source["url"].startswith("https://"))
            self.assertEqual(source["checked_at"], "2026-08-26")


if __name__ == "__main__":
    unittest.main()
