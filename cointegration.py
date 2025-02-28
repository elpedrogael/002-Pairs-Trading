import numpy as np
import pandas as pd
from statsmodels.tsa.vector_ar.vecm import coint_johansen, VECM
from kalman_filter import KalmanFilter

def check_cointegration(data):
    result = coint_johansen(data, det_order=0, k_ar_diff=1)
    return result.lr1[0] > result.cvt[0, 0]

def calculate_hedge_ratio(data):
    kf = KalmanFilter()
    hedge_ratios = []

    for x, y in zip(prices_x, prices_y):
        kf.predict()
        kf.update(x, y)
        hedge_ratios.append(kf.get_hedge_ratio())

    return np.array(hedge_ratios)

def generate_signals(data):
    model = VECM(data, k_ar_diff=1, coint_rank=1)
    results = model.fit()
    spread = results.resid
    signals = np.where(spread > 1.5 * spread.std(), -1, np.where(spread < -1.5 * spread.std(), 1, 0))
    return signals