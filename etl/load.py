from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()


def get_engine():

    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    database_url = (
        f"postgresql+psycopg2://"
        f"{user}:{password}@"
        f"{host}:{port}/{database}"
    )

    return create_engine(database_url)


def load_sales_data(df):

    engine = get_engine()

    df.to_sql(
        "sales",
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} rows into PostgreSQL table 'sales'.")

if __name__ == "__main__":
    from extract import extract_csv
    from validate import validate_sales_data
    from transform import transform_sales_data

    df = extract_csv("data/raw/sales.csv")
    df = validate_sales_data(df)
    df = transform_sales_data(df)

    load_sales_data(df)