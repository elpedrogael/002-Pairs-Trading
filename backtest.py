import pandas as pd
import matplotlib.pyplot as plt
import python_ta
#python_ta.check_all()

data = pd.read_csv("data/historical_data.csv").dropna()
data.head()

rsi = (ta.momentum.RSIIndicator(data.Close, window=50))

capital = 1_000_000
com = 0.125 / 100
n_shares = 20
active_positions = []
active_short_postions = []
active_long_postions = []

portfolio_value = []

for i, row in data.iterrows():
    # Close long positions
    if row.RSI > 50:
        for position in active_positions:
            capital += (n_shares * row.Close) * (1 - com)
        active_positions = []

    # Buy if we have enough cash
    if row.BUY_SIGNAL:
        operation_cost = n_shares * row.Close * (1 + com)
        if capital > operation_cost:
            capital -= operation_cost
            active_positions.append({
                "date": row.Datetime,
                "bought_at": row.Close,
                "shares": n_shares
            })

    # Calculate portfolio value
    active_ops = len(active_positions)
    total_shares = active_ops * n_shares
    current_value = total_shares * row.Close
    portfolio_value.append(current_value + capital)