from math import sin, sqrt

from scipy.optimize import fsolve

from OrbitalBody import OrbitalBody


class Orbit:
    def __init__(
        self,
        inclination: float,
        rightAscensionOfAscendingNode: float,
        argumentOfPeriapsis: float,
        maxAltitude: float,
        eccentricity: float,
        orbitalBody: OrbitalBody,
    ):
        self.inclination = inclination
        self.rightAscensionOfAscendingNode = rightAscensionOfAscendingNode
        self.argumentOfPeriapsis = argumentOfPeriapsis
        self.maxAltitude = maxAltitude
        self.eccentricity = eccentricity
        self.orbitalBody = orbitalBody
        self.semiMajorAxis = _getSemiMajorAxis(self)

    def _getEccentricAnomalyCoefficient(self) -> float:
        return sqrt(pow(self.semiMajorAxis, 3) / self.orbitalBody.gravitationalParamter)

    def getEccentricAnomaly(self, time: float) -> float:
        return _getEccentricAnomaly(self, time)


def _getSemiMajorAxis(orbit: Orbit) -> float:
    return (orbit.orbitalBody.radius + orbit.maxAltitude) / (1 + orbit.eccentricity)


def _getEccentricAnomaly(orbit: Orbit, time: float) -> float:
    coefficient = orbit._getEccentricAnomalyCoefficient()

    def _eccentricAnomalyAndTimeFunction(E: float) -> float:
        return coefficient * (E - orbit.eccentricity * sin(E)) - time

    # The estimated root is obtained by using the approximation sin(E) ~ E.
    estimatedRoot = time / (coefficient * (1 - orbit.eccentricity))
    root: float = fsolve(_eccentricAnomalyAndTimeFunction, estimatedRoot)[0]
    return root
