import numpy as np
import pandas as pd
from statsmodels.tsa.vector_ar.vecm import coint_johansen
from kalman_filter import KalmanFilter

def check_cointegration(data):
    result = coint_johansen(data, det_order=0, k_ar_diff=1)
    return result.lr1[0] > result.cvt[0, 0]  # Check if cointegrated

def calculate_hedge_ratio(data):
    kf = KalmanFilter()
    hedge_ratios = []

    for x, y in zip(prices_x, prices_y):
        kf.predict()
        kf.update(x, y)
        hedge_ratios.append(kf.get_hedge_ratio())

    return np.array(hedge_ratios)