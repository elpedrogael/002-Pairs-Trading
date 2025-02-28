import pandas as pd

def process_data(file_path= "data/historical_data.csv"):
    data = pd.read_csv("data/historical_data.csv")
    data_cleaned = data.iloc[1:].reset_index(drop=True)
    data_cleaned["Date"] = pd.to_datetime(data_cleaned["Date"])
    numeric_columns = ['Close', 'Close.1', 'High', 'High.1', 'Low', 'Low.1', 'Open', 'Open.1', 'Volume', 'Volume.1']
    data_cleaned[numeric_columns] = data_cleaned[numeric_columns].astype(float)
    return data_cleaned

if __name__ == "__main__":
    file_path = "data/historical_data.csv"
    data_cleaned = process_data(file_path)
    data_cleaned.to_csv('data/processed_data.csv', index=False)