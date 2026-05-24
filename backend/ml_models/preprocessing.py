import pandas as pd

def load_data():
    df = pd.read_csv("datasets/supply_chain_data.csv")

    # Convert date column
    df["date"] = pd.to_datetime(df["date"])

    # Handle missing values
    df.fillna(0, inplace=True)

    return df

if __name__ == "__main__":
    data = load_data()
    print(data.head())