import numpy as np
import matplotlib.pyplot as plt

class KalmanFilter:
    def __init__(self):
        self.x = np.array([1, 1]) #initial observation
        self.A = np.eye(2) #Transition matrix
        self.Q = np.eye(2) * 0.1 #covariance matrix in estimations
        self.R = np.array([[1]]) * 0.001 #Errors in observations - TUNE
        self.P = np.eye(2) * 10 #Predicted error covariance matrix

    def predict(self):
        self.P = self.A @ self.P @ self.A.T + self.Q

    def update(self, x, y):
        C = np.array([[1, x]])  # Observations (1, 2)
        S = C @ self.P @ C.T + self.R
        K = self.P @ C.T @ np.linalg.inv(S)  # Kalman gain
        self.x = self.x + K @ (y - C @ self.x)
        self.P = (np.eye(2) - K @ C) @ self.P

    def get_hedge_ratio(self):
        return self.x[1]
