import argparse
from src.pipeline import run_pipeline


def main():
    parser = argparse.ArgumentParser(
        description="GenAI Mini ETL Pipeline"
    )

    parser.add_argument(
        "--input",
        default="data/input.csv",
        help="Path to input CSV file"
    )

    parser.add_argument(
        "--output",
        default="output/results.csv",
        help="Path to output CSV file"
    )

    parser.add_argument(
        "--threshold",
        type=int,
        default=80,
        help="Score threshold for passing"
    )

    args = parser.parse_args()

    run_pipeline(
        input_path=args.input,
        output_path=args.output,
        threshold=args.threshold,
    )


if __name__ == "__main__":
    main()