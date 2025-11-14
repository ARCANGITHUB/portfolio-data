import pandas as pd
import sqlite3
import argparse


def etl_process(input_file, db_file):
    # Extract
    df = pd.read_csv(input_file)

    # Transform
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['ship_date'] = pd.to_datetime(df['ship_date'])

    # Drop unnecessary columns
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    # Derive unit_price if missing
    if 'unit_price' not in df.columns and 'sales' in df.columns and 'quantity' in df.columns:
        df['unit_price'] = df['sales'] / df['quantity']

    # Load
    conn = sqlite3.connect(db_file)
    df.to_sql('sales', conn, if_exists='replace', index=False)
    conn.close()

    print(f"ETL complete! Data writen to {db_file} (table: sales)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--db", required=True, help="Path to SQLite DB")
    args = parser.parse_args()

    etl_process(args.input, args.db)
