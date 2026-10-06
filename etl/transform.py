import pandas as pd


def transform_sales_data(df):

    df = df.copy()

    df["order_date"] = pd.to_datetime(df["order_date"])

    df["sales_amount"] = (
        df["quantity"] * df["unit_price"]
    )

    print("Transformation successful.")

    return df


if __name__ == "__main__":
    from extract import extract_csv
    from validate import validate_sales_data

    df = extract_csv("data/raw/sales.csv")
    df = validate_sales_data(df)
    df = transform_sales_data(df)

    print("\nTransformed data:")
    print(df)