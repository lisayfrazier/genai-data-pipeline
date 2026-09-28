"""Coordinate extraction, validation, transformation, and reports."""

from pathlib import Path

from src.extract import extract_from_csv
from src.load import write_csv
from src.transform import add_passed_flag


def run_pipeline(input_path, output_path, report_path, threshold):
    if not 0 <= threshold <= 100:
        raise ValueError("threshold must be between 0 and 100")
    paths = [Path(p).resolve() for p in (input_path, output_path, report_path)]
    if len(set(paths)) != 3:
        raise ValueError("input, output, and report paths must be different")

    valid, errors = extract_from_csv(input_path)
    write_csv(add_passed_flag(valid, threshold), output_path,
              ["name", "score", "passed"])
    write_csv(errors, report_path, ["row_number", "name", "score", "error"])
    return len(valid), len(errors)
