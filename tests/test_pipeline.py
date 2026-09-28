import csv
import tempfile
import unittest
from pathlib import Path

from main import main
from src.pipeline import run_pipeline


class PipelineTests(unittest.TestCase):
    def test_mixed_rows_produce_results_and_report(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "input.csv"
            source.write_text("name,score\nAlice,92\nBob,abc\n,78\nCara,101\nDan,80\n", encoding="utf-8")
            output, report = root / "out" / "results.csv", root / "out" / "errors.csv"
            self.assertEqual((2, 3), run_pipeline(source, output, report, 80))
            with output.open(newline="") as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(["Alice", "Dan"], [r["name"] for r in rows])
            self.assertEqual(["True", "True"], [r["passed"] for r in rows])
            with report.open(newline="") as stream:
                errors = list(csv.DictReader(stream))
            self.assertEqual(["3", "4", "5"], [r["row_number"] for r in errors])
            self.assertIn("integer", errors[0]["error"])

    def test_missing_header_does_not_write_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "input.csv"
            source.write_text("name,points\nAlice,91\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "score"):
                run_pipeline(source, root / "results.csv", root / "report.csv", 80)
            self.assertFalse((root / "results.csv").exists())

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "input.csv"
            source.write_text("name,score\nAlice,90\n", encoding="utf-8")
            args = ["--input", str(source), "--output", str(root / "out.csv"),
                    "--report", str(root / "report.csv")]
            self.assertEqual(0, main(args))
            source.write_text("name,score\nAlice,bad\n", encoding="utf-8")
            self.assertEqual(1, main(args))
            self.assertEqual(2, main(args + ["--threshold", "101"]))


if __name__ == "__main__":
    unittest.main()
