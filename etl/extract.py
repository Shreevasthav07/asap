from sources.csv_reader import read_csv
from sources.excel_reader import read_excel
from pathlib import Path

def extract_file(file_path):
    file_path = Path(file_path)
    if file_path.suffix.lower() == ".csv":
        return read_csv(file_path)

    elif file_path.suffix.lower() in [".xlsx", ".xls"]:
        return read_excel(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {file_path.suffix}"
        )