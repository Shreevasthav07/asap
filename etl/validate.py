def validate_sales_data(df):

    required_columns = [
        "order_id",
        "order_date",
        "customer_id",
        "product_id",
        "quantity",
        "unit_price"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if df.empty:
        raise ValueError("The input dataset is empty.")

    if df["order_id"].duplicated().any():
        raise ValueError("Duplicate order_id values found.")

    if (df["quantity"] <= 0).any():
        raise ValueError("Quantity must be greater than zero.")

    if (df["unit_price"] < 0).any():
        raise ValueError("Unit price cannot be negative.")

    print("Validation successful.")

    return df

if __name__ == "__main__":
    from extract import extract_csv

    df = extract_csv("data/raw/sales.csv")
    validate_sales_data(df)