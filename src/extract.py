"""Read and validate score records from a CSV file."""

import csv


REQUIRED_COLUMNS = {"name", "score"}


def extract_from_csv(path):
    """Return valid records and row-level errors (using physical CSV line numbers)."""
    valid, errors = [], []
    with open(path, "r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames is None:
            raise ValueError("Input CSV is empty or has no header")
        missing = REQUIRED_COLUMNS - set(reader.fieldnames)
        if missing:
            raise ValueError("Input CSV missing required column(s): " + ", ".join(sorted(missing)))
        for row in reader:
            line = reader.line_num
            name = (row.get("name") or "").strip()
            raw_score = (row.get("score") or "").strip()
            problems = []
            if not name:
                problems.append("name is required")
            try:
                score = int(raw_score)
            except ValueError:
                problems.append("score must be an integer")
                score = None
            if score is not None and not 0 <= score <= 100:
                problems.append("score must be between 0 and 100")
            if None in row:
                problems.append("too many fields")
            if problems:
                errors.append({"row_number": line, "name": name, "score": raw_score,
                               "error": "; ".join(problems)})
            else:
                valid.append({"name": name, "score": score})
    return valid, errors
