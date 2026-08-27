import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "data" / "robotics_normative_snapshot_20260826.v3.json"
DOC = ROOT / "docs" / "ROBOTICS_NORMATIVE_CONTINUOUS_EVOLUTION_V3.md"


class RoboticsNormativeSnapshotV3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with SNAPSHOT.open("r", encoding="utf-8") as handle:
            cls.snapshot = json.load(handle)

    def test_snapshot_is_date_bounded(self):
        self.assertEqual(self.snapshot["checked_at"], "2026-08-26")
        self.assertEqual(self.snapshot["state"], "CURRENT_BOUNDED")

    def test_current_brazilian_regulatory_deltas_are_present(self):
        ids = {source["id"] for source in self.snapshot["sources"]}
        for required in {
            "BR-ANPD-R15-2024",
            "BR-ANPD-R18-2024",
            "BR-ANPD-R19-2024",
            "BR-ECA-DIGITAL-15211-2025",
            "BR-LAW-15352-2026",
            "BR-ANPD-R30-2025",
            "BR-ANPD-R31-2025",
            "BR-ANPD-R32-2026",
        }:
            self.assertIn(required, ids)

    def test_eu_ai_act_timing_is_not_collapsed(self):
        timeline = self.snapshot["timelines"]
        self.assertEqual(timeline["EU_AI_Act_general_application"], "2026-08-02")
        self.assertEqual(timeline["EU_AI_Act_Annex_III_high_risk"], "2027-12-02")
        self.assertEqual(timeline["EU_AI_Act_Annex_I_product_high_risk"], "2028-08-02")

    def test_current_standard_versions_are_explicit(self):
        ids = {source["id"] for source in self.snapshot["sources"]}
        for required in {
            "ISO-IEC-27701-2025",
            "ISO-14001-2026",
            "ISO-IEC-42001-2023",
            "ISO-8000-1-2022",
            "IEEE-7000-2021",
            "IEEE-7002-2022",
            "IEEE-7003-2024",
            "IEEE-7007-2021",
            "IEEE-7009-2024",
            "RFC-6973",
            "RFC-3552",
        }:
            self.assertIn(required, ids)

    def test_non_regression_preserves_unknowns_and_authority_types(self):
        invariants = set(self.snapshot["non_regression_invariants"])
        self.assertIn("TOKEN_VAZIO_NOT_ERASED", invariants)
        self.assertIn("AUTHORITY_TYPE_REQUIRED", invariants)
        self.assertIn("STANDARD_NOT_PROMOTED_TO_STATUTE", invariants)
        self.assertIn("NORMATIVE_CHANGE_REOPENS_IMPACTED_GATES", invariants)
        self.assertTrue(all(token["state"] == "TOKEN_VAZIO" for token in self.snapshot["open_tokens"]))

    def test_frontier_document_contains_falsifiable_boundaries(self):
        text = DOC.read_text(encoding="utf-8")
        for marker in [
            "FONTE",
            "TOKEN_VAZIO != NÃO",
            "CONCENTRATION != CARTEL",
            "NORMATIVE_STATE_2024 != NORMATIVE_STATE_2026",
            "MUDANÇA SEM REVALIDAÇÃO = REGRESSÃO POTENCIAL",
        ]:
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
