from extract import extract_csv
from validate import validate_sales_data
from transform import transform_sales_data
from load import load_sales_data


def run_pipeline():

    file_path = "data/raw/sales.csv"

    print("\n--- SALES ETL PIPELINE ---")

    df = extract_csv(file_path)

    df = validate_sales_data(df)

    df = transform_sales_data(df)

    load_sales_data(df)

    print("--- PIPELINE COMPLETED ---\n")


if __name__ == "__main__":
    run_pipeline()