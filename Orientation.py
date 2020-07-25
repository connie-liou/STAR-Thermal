from enum import Enum


class ZAxisOrientation:
    def __init__(self, rightAscension: float, declination: float):
        self.rightAscension = rightAscension
        self.declination = declination


class LocalAxis(Enum):
    X = 1
    Y = 2
    Z = 3


class AdditionalRotation:
    def __init__(self, rotationRate: float, localAxis: LocalAxis):
        self.rotationRate = rotationRate
        self.localAxis = localAxis


class Orientation:
    def __init__(
        self,
        zAxisInitialOrientation: ZAxisOrientation,
        additionalRotation: AdditionalRotation,
    ):
        self.zAxisInitialOrientation = zAxisInitialOrientation
        self.additionalRotation = additionalRotation
