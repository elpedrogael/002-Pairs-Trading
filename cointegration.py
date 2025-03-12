import numpy as np
import statsmodels.api as sm

def calculate_spread(data1, data2):
    hedge_ratio = np.polyfit(data1, data2, 1)[0]
    spread = data2 - hedge_ratio * data1
    spread_norm = (spread - spread.mean()) / spread.std()
    return hedge_ratio, spread, spread_norm
