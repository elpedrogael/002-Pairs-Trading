import pandas as pd
import numpy as np


def backtest_strategy(data, capital=1_000_000, com=0.00125):
    # Calculate spread and trading signals
    data['Spread'] = data['Close'] - data['Hedge Ratio'] * data['Close.1']
    data['Z-Score'] = (data['Spread'] - data['Spread'].mean()) / data['Spread'].std()

    # Generate signals
    data['Long Signal'] = data['Z-Score'] < -1.5
    data['Short Signal'] = data['Z-Score'] > 1.5

    # Backtest logic
    active_positions = []
    portfolio_value = [capital]

    for i, row in data.iterrows():
        # Close positions
        if abs(row['Z-Score']) < 0.5:
            for position in active_positions:
                capital += (position['shares'] * row['Close']) * (1 - com)
            active_positions = []

        # Open long positions
        if row['Long Signal']:
            operation_cost = row['Close'] * (1 + com)
            if capital > operation_cost:
                capital -= operation_cost
                active_positions.append({'shares': 1, 'price': row['Close']})

        # Open short positions
        if row['Short Signal']:
            operation_cost = row['Close'] * (1 + com)
            if capital > operation_cost:
                capital -= operation_cost
                active_positions.append({'shares': -1, 'price': row['Close']})

        # Update portfolio value
        portfolio_value.append(capital + sum([pos['shares'] * row['Close'] for pos in active_positions]))

    return portfolio_value