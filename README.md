# Python CSV Data Pipeline (Mini ETL)

A small Python project demonstrating an extract, transform, and load workflow. It reads names and scores from a CSV file, converts each score to an integer, adds a pass/fail flag, and writes a new CSV file.

This is a learning project. It does not call an LLM or run a production GenAI service.

## Run

From the repository root, with Python 3 installed:

```bash
python main.py
```

By default, the script reads `data/input.csv`, writes `output/results.csv`, and uses a threshold of 80. Customize the paths and threshold:

```bash
python main.py --input data/input.csv --output output/results.csv --threshold 80
```

The input must include `name` and `score` columns, and score values must be convertible to integers. The output contains `name`, `score`, and `passed`. Invalid or missing score data currently raises an error; the project does not yet provide a separate validation report.

## Structure

- `main.py` parses command-line options.
- `src/extract.py` reads CSV rows.
- `src/transform.py` adds the pass flag.
- `src/load.py` writes the result.
- `src/pipeline.py` connects the steps.

Created by [Lisa Y. Frazier](https://github.com/lisayfrazier).
