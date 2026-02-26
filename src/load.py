import csv
import os
from typing import List, Dict, Any


def load_to_csv(data: List[Dict[str, Any]], path: str):
    """Write rows to a CSV file."""

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["name", "score", "passed"]
        )
        writer.writeheader()
        writer.writerows(data)
