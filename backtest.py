import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ta

data = pd.read_csv("data/historical_data.csv").dropna()
data["Date"] = pd.to_datetime(data["Date"])  # Ensure Date column is datetime
data["Close"] = pd.to_numeric(data["Close"], errors='coerce')
data = data.dropna(subset=['Close'])

rsi = ta.momentum.RSIIndicator(data["Close"], window=50)
data["RSI"] = rsi.rsi()
data = data.dropna()

#SIGNALS
data["BUY_SIGNAL"] = data["RSI"] < 30
data["SELL_SIGNAL"] = data["RSI"] > 70

buy_dates = data.loc[data["BUY_SIGNAL"], "Date"]
buy_prices = data.loc[data["BUY_SIGNAL"], "Close"]
sell_dates = data.loc[data["SELL_SIGNAL"], "Date"]
sell_prices = data.loc[data["SELL_SIGNAL"], "Close"]

plt.figure(figsize=(12, 6))
plt.plot(data["Date"], data["Close"], label="Stock Price", color='blue', linewidth=1.5)
plt.scatter(buy_dates, buy_prices, marker='^', color='green', label="Buy Signal", s=100)
plt.scatter(sell_dates, sell_prices, marker='v', color='red', label="Sell Signal", s=100)
plt.title("Stock Price with Buy/Sell Signals (RSI Strategy)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid()
plt.show()

