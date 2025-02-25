import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/historical_data.csv"
data_cleaned = pd.read_csv(file_path)

data_cleaned['Date'] = pd.to_datetime(data_cleaned['Date'])

plt.figure(figsize=(12, 6))
plt.plot(data_cleaned['Date'], data_cleaned['Close'], label="AAPL", color='blue')
plt.plot(data_cleaned['Date'], data_cleaned['Close.1'], label="MSFT", color='red')

plt.title("Precios de Cierre de AAPL y MSFT (2014 - 2024)")
plt.xlabel("Fecha")
plt.ylabel("Precio de Cierre (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


file_path = "data/historical_data.csv"
data = pd.read_csv(file_path)

data['Date'] = pd.to_datetime(data['Date'])

plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Close'], label="AAPL", color='blue')
plt.plot(data['Date'], data['Close.1'], label="MSFT", color='red')

plt.title("Precios de Cierre de AAPL y MSFT (2014 - 2024)")
plt.xlabel("Fecha")
plt.ylabel("Precio de Cierre (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
