import pandas as pd

file_path = "data/historical_data.csv"
data = pd.read_csv(file_path)

data_info = data.info()
data_head = data.head()

missing_values = data.isnull().sum()

columns = data.columns

data_info, data_head, missing_values, columns

#

data_cleaned = data.iloc[2:].reset_index(drop=True)

numeric_columns = ['Close', 'Close.1', 'High', 'High.1', 'Low', 'Low.1', 'Open', 'Open.1', 'Volume', 'Volume.1']
data_cleaned[numeric_columns] = data_cleaned[numeric_columns].astype(float)

data_cleaned = data_cleaned.dropna()

data_cleaned.head()

data_cleaned = data_cleaned.rename(columns={'Price': 'Date'})
data_cleaned['Date'] = pd.to_datetime(data_cleaned['Date'])

data_cleaned.head()
