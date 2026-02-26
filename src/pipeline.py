from src.extract import extract_from_csv
from src.transform import add_passed_flag
from src.load import load_to_csv


def run_pipeline(input_path, output_path, threshold):
    print("Pipeline starting...")

    data = extract_from_csv(input_path)

    transformed = add_passed_flag(data, threshold)

    load_to_csv(transformed, output_path)

    print(f"Pipeline completed. Wrote: {output_path}")