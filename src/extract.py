import csv
from typing import List, Dict, Any


def extract_from_csv(path: str) -> List[Dict[str, Any]]:
    """Read rows from a CSV file."""
    
    data = []

    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["score"] = int(row["score"])
            data.append(row)

    return data
