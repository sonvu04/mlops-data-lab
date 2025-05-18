import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    return df.dropna()

def feature_engineering(df):
    # Add a feature: tip percentage
    df['bill_with_tip'] = df['total_bill'] + df['tip']
    return df

if __name__ == "__main__":
    df = load_data("data/raw/tips.csv")
    df = clean_data(df)
    df = feature_engineering(df)
    df.to_csv("data/processed/tips_clean.csv", index=False)
    print("ETL completed. Cleaned file saved.")
