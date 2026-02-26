from typing import List, Dict, Any


def add_passed_flag(data: List[Dict[str, Any]], threshold: int = 80):
    """Add a passed=True/False field based on score."""
    
    for row in data:
        row["passed"] = row["score"] >= threshold

    return data
