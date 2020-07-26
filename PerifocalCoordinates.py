import numpy as np


class PerifocalCoordinates:
    def __init__(self, P: float, Q: float, W: float):
        self.P = P
        self.Q = Q
        self.W = W

    def getCoordinateVector(self) -> np.array:
        return np.array([self.P, self.Q, self.W])
