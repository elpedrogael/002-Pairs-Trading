import numpy as np
import matplotlib.pyplot as plt

class KalmanFilter:
    def __init__(self):
        self.x = np.array([1, 1]) #initial observation
        self.A = np.eye(2) #Transition matrix
        self.Q = np.eye(2) * 0.1 #covariance matrix in estimations
        self.R = np.array([[1]]) * 0.001 #Errors in observations - TUNE
        self.P = np.eye(2) * 10 #Predicted error covariance matrix

    def update(self, x, y):
        C = np.array([[1, x]])  # Observations (1, 2)
        S = C @ self.P @ C.T + self.R
        K = self.P @ C.T @ np.linalg.inv(S)  # Kalman gain
        self.P = (np.eye(2) - K @ C) @ self.P
        self.x = self.x + K @ (y - C @ self.x)

    def predict(self):
        self.P = self.A @ self.P @ self.A.T + self.Q
#** TOCHECK
kalman_linear = KalmanFilter()
kalman_preds = []
for i in range(len(xl)):
    kalman_linear.predict()
    x_ = xl[i]
    y_ = yl[i]
    kalman_linear.update(x_, y_)
    params = kalman_linear.x
    kalman_preds.append(params[0] + params[1] * x_)
#**
plt.figure(figsize = (12,5))
plt.scatter(xl,yl)
plt.plot(xl, kalman_preds, 'r')
plt.legend()
plt.show()