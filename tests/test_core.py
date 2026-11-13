import unittest
import pandas as pd
from src.core import analyze, validate


class TestCore(unittest.TestCase):
    def test_scoring(self):
        df = pd.DataFrame({
            "timestamp": pd.date_range("2026-01-01", periods=100, freq="h").astype(str),
            "asset_id": ["P-101"] * 100,
            "vibration_mm_s": [2 + i * .01 for i in range(100)]
        })
        out, audit = analyze(df, sensors=["vibration_mm_s"])
        self.assertEqual(len(out), 100)
        self.assertTrue((out["status"] == "scored").all())
        self.assertGreaterEqual(int(out["is_anomaly"].sum()), 1)
        self.assertEqual(len(audit), 1)

    def test_duplicates(self):
        df = pd.DataFrame({
            "timestamp": ["2026-01-01", "2026-01-01"],
            "asset_id": ["P", "P"], "vibration_mm_s": [1, 2]
        })
        with self.assertRaises(ValueError):
            validate(df)

    def test_short_input(self):
        df = pd.DataFrame({
            "timestamp": pd.date_range("2026-01-01", periods=4, freq="h").astype(str),
            "asset_id": ["P"] * 4, "vibration_mm_s": [1, 2, 3, 4]
        })
        out, _ = analyze(df)
        self.assertTrue((out["status"] == "insufficient_data").all())

    def test_missing_columns(self):
        with self.assertRaises(ValueError):
            validate(pd.DataFrame({"sensor": [1, 2]}))

    def test_nonfinite_sensor(self):
        df = pd.DataFrame({
            "timestamp": pd.date_range("2026-01-01", periods=100, freq="h").astype(str),
            "asset_id": ["P"] * 100,
            "vibration_mm_s": [float("inf")] + list(range(99))
        })
        out, _ = analyze(df)
        self.assertEqual(int((out["status"] == "missing_sensor_values").sum()), 1)


if __name__ == "__main__":
    unittest.main()
