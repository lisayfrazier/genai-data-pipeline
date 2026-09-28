# Python CSV Data Pipeline (Mini ETL)

A Python learning project that validates score records, transforms valid rows, and writes both results and a row-level validation report. It demonstrates a small extract, transform, and load workflow; it does not use a language model or run a production AI service.

## Run it

Python 3 is required; this project uses only the standard library. From the repository root:

```bash
python main.py
```

The default sample `data/input.csv` includes one invalid score. The command reports **2 valid, 1 invalid**, writes `output/results.csv`, and writes `output/validation_report.csv`. An exit status of 1 is expected for this sample because it contains an invalid row.

To use your own input and passing threshold:

```bash
python main.py --input data/input.csv --output output/results.csv --report output/validation_report.csv --threshold 80
```

Input columns: `name,score`. Names must be nonempty; scores must be whole numbers from 0 to 100. The valid result has `name,score,passed`. The report has `row_number,name,score,error`, so you can find and correct rejected rows in the input file. Blank names, invalid or out-of-range scores, and extra fields are reported without stopping valid rows from processing. Missing required columns, missing input files, invalid thresholds, or overlapping input/output/report paths stop the run with a clear error.

Exit codes: **0** = all rows valid, **1** = report contains invalid rows, **2** = pipeline could not run. Generated files in `output/` are excluded from Git.

## Example

With the included sample, the results file contains Bob (92, passed) and Charlie (78, not passed). The validation report identifies Alice's nonnumeric score on line 2.

## Test

```bash
python -m unittest discover -s tests -v
```

Tests cover mixed valid and invalid data, missing columns, and command line exit codes.

## Code map

- `main.py` parses arguments, prints a summary, and sets exit status.
- `src/extract.py` reads CSV rows and validates fields.
- `src/transform.py` applies the passing threshold.
- `src/load.py` writes CSV files.
- `src/pipeline.py` coordinates the steps and prevents path collisions.

Created by [Lisa Y. Frazier](https://github.com/lisayfrazier).
