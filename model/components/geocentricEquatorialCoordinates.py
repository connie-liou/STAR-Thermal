import numpy as np


class GeocentricEquatorialCoordinates:
    def __init__(self, I: float, J: float, K: float):
        self.I = I
        self.J = J
        self.K = K

    def getCoordinateVector(self) -> np.array:
        return np.array([self.I, self.J, self.K])
