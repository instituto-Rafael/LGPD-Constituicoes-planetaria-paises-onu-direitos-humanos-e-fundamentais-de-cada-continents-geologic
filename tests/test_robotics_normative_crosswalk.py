import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "robotics_normative_crosswalk_v2.json"


def load_registry():
    with REGISTRY.open("r", encoding="utf-8") as handle:
        return json.load(handle)


class RoboticsNormativeCrosswalkTests(unittest.TestCase):
    def test_core_invariants_protect_user_and_evidence_boundaries(self):
        registry = load_registry()
        invariants = set(registry["core_invariants"])
        self.assertIn("TOKEN_VAZIO != false", invariants)
        self.assertIn("ACKNOWLEDGED != CONSENT", invariants)
        self.assertIn("USER_SOVEREIGNTY != CONSENT_ONLY", invariants)
        self.assertIn("USER_PREFERENCE != LEGAL_OVERRIDE", invariants)
        self.assertIn("REFERENCE != CERTIFICATION", invariants)
        self.assertIn("market_concentration != cartel_proof", invariants)

    def test_lgpd_contains_core_robotics_articles(self):
        registry = load_registry()
        articles = {item["article"] for item in registry["brazil"]["lgpd"]}
        required = {"6", "7", "8", "9", "18", "20", "37", "38", "46", "48", "49", "50", "51"}
        self.assertTrue(required.issubset(articles))

    def test_current_normative_references_are_versioned(self):
        standards = {item["id"]: item for item in load_registry()["standards"]}
        self.assertIn("ISO-IEC-27001-2022", standards)
        self.assertIn("ISO-IEC-27701-2025", standards)
        self.assertIn("ISO-14001-2026", standards)
        self.assertIn("NIST-CSF-2.0", standards)
        self.assertIn("IEEE-7003-2024", standards)
        self.assertIn("RFC-6973", standards)

    def test_two_audit_claim_is_not_promoted_without_source(self):
        examples = {item["id"]: item for item in load_registry()["assurance_examples"]}
        self.assertEqual(examples["TWO-EXTERNAL-AUDITS-ALL-LISTED"]["state"], "TOKEN_VAZIO")

    def test_serious_systemic_claims_fail_closed(self):
        policy = load_registry()["serious_claim_policy"]
        self.assertEqual(policy["default_state"], "TOKEN_VAZIO")
        self.assertIn("sovereignty_violation", policy["claims"])
        self.assertIn("financial_market_manipulation", policy["claims"])
        self.assertIn("attack_on_global_financial_system", policy["claims"])
        self.assertGreaterEqual(len(policy["minimum_evidence"]), 8)

    def test_mapa_enrollment_is_not_faked(self):
        registry = load_registry()
        self.assertEqual(registry["federation"]["producer_enrollment"], "TOKEN_VAZIO")
        self.assertEqual(registry["gates"]["G-NORM-07_mapa_producer_enrollment"], "TOKEN_VAZIO")


if __name__ == "__main__":
    unittest.main()
