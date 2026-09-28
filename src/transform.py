"""Apply a pass threshold to validated score records."""


def add_passed_flag(data, threshold=80):
    return [{**row, "passed": row["score"] >= threshold} for row in data]
