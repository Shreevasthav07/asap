from extract import extract_file
from validate import validate_sales_data
from transform import transform_sales_data
from load import load_sales_data
import argparse


def run_pipeline(file_path):
    
    print("\n--- SALES ETL PIPELINE ---")

    df = extract_file(file_path)

    df = validate_sales_data(df)

    df = transform_sales_data(df)

    load_sales_data(df)

    print("--- PIPELINE COMPLETED ---\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the sales ETL Pipeline"
    )
    parser.add_argument(
        "file_path",
        help = "Path to the CSV File"
    )
    args = parser.parse_args()

    run_pipeline(args.file_path)