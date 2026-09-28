"""Run the CSV validation pipeline from the command line."""

import argparse
import csv
import sys

from src.pipeline import run_pipeline


def main(argv=None):
    parser = argparse.ArgumentParser(description="CSV score validation and mini ETL")
    parser.add_argument("--input", default="data/input.csv", help="Input CSV path")
    parser.add_argument("--output", default="output/results.csv", help="Valid results CSV path")
    parser.add_argument("--report", default="output/validation_report.csv",
                        help="Invalid rows report CSV path")
    parser.add_argument("--threshold", type=int, default=80, help="Passing score, 0–100")
    args = parser.parse_args(argv)
    try:
        valid, invalid = run_pipeline(args.input, args.output, args.report, args.threshold)
    except (OSError, ValueError, csv.Error) as exc:
        print(f"Pipeline error: {exc}", file=sys.stderr)
        return 2
    print(f"Processed {valid + invalid} rows: {valid} valid, {invalid} invalid.")
    print(f"Results: {args.output}\nValidation report: {args.report}")
    return 1 if invalid else 0


if __name__ == "__main__":
    sys.exit(main())
