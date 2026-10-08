from pathlib import Path
import pandas as pd


def read_csv(file_path):

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    if file_path.suffix.lower() != ".csv":
        raise ValueError(
            f"Expected a CSV file, got: {file_path.suffix}"
        )

    df = pd.read_csv(file_path)

    print(
        f"Extracted {len(df)} rows from {file_path.name}"
    )

    return df