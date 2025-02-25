import yfinance as yf
import pandas as pd

def download_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    data.reset_index(inplace=True)  # Asegura que la fecha sea una columna
    data.to_csv('data/historical_data.csv', index=False)  # Guarda correctamente

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT']  # Activos a analizar
    start_date = '2014-01-01'
    end_date = '2024-01-01'
    download_data(tickers, start_date, end_date)
