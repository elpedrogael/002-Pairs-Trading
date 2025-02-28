import pandas as pd
from kalman_filter import KalmanFilter
from cointegration import check_cointegration, calculate_hedge_ratio
from backtest import backtest_strategy
from data_process import process_data


def main():
    data = process_data()

    if check_cointegration(data):
        hedge_ratios = calculate_hedge_ratio(data['Close'], data['Close.1'])
        backtest_strategy(data, hedge_ratios.mean())
    else:
        print("The selected assets are not cointegrated.")


if __name__ == "__main__":
    main()
