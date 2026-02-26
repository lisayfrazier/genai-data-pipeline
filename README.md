# GenAI Data Pipeline (Mini ETL)

A simple ETL pipeline in Python that:
- Extracts rows from `data/input.csv`
- Transforms the data by adding a `passed` flag based on a score threshold
- Loads output to `output/results.csv`

## How to Run
```bash
py main.py
## Data Validation

The pipeline performs strict validation:
- Ensures required columns exist
- Ensures score values are integers
- Fails fast on corrupted data

This mirrors real-world AI system data integrity safeguards.