from pathlib import Path
import pandas as pd


def extract_csv(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)

    print(f"Extracted {len(df)} rows from {file_path.name}")

    return df

if __name__ == "__main__":
    df = extract_csv("data/raw/sales.csv")

    print("\nFirst 5 rows:")
    print(df.head())