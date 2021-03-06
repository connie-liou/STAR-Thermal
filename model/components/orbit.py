from math import sin, sqrt, cos, pi, acos

import numpy as np
from scipy.optimize import fsolve

from model.components.orbitalBody import OrbitalBody
from model.components.perifocalCoordinates import PerifocalCoordinates
from model.components.geocentricEquatorialCoordinates import (
    GeocentricEquatorialCoordinates,
)


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
        self.transformationMatrix = self._getTransformationMatrix()

    def _getEccentricAnomalyCoefficient(self) -> float:
        return sqrt(pow(self.semiMajorAxis, 3) / self.orbitalBody.gravitationalParamter)

    def getEccentricAnomaly(self, time: float) -> float:
        return _getEccentricAnomaly(self, time)

    def getTrueAnomaly(self, eccentricAnomaly: float) -> float:
        """This function covers equations 2.25 and 2.26 in the thermal
        analysis paper
        """
        cosTrueAnomaly = (self.eccentricity - cos(eccentricAnomaly)) / (
            self.eccentricity * cos(eccentricAnomaly) - 1
        )
        if eccentricAnomaly <= pi:
            result = acos(cosTrueAnomaly)
        else:
            result = 2 * pi - acos(cosTrueAnomaly)
        return result

    def getDistanceFromOrbitalBody(self, eccentricAnomaly: float) -> float:
        return self.semiMajorAxis * (1 - self.eccentricity * cos(eccentricAnomaly))

    def getPerifocalCoordinates(
        self, distance: float, trueAnomaly: float
    ) -> PerifocalCoordinates:
        return PerifocalCoordinates(
            distance * cos(trueAnomaly), distance * sin(trueAnomaly), 0
        )

    def _getTransformationMatrix(self) -> np.ndarray:
        """This matrix is used to convert Perifocal Coordinates to 
        Geocentric-Equatorial Coordinates.
        """
        omega = self.rightAscensionOfAscendingNode
        i = self.inclination
        w = self.argumentOfPeriapsis
        return np.array(
            [
                [
                    cos(omega) * cos(w) - sin(omega) * sin(w) * cos(i),
                    -cos(omega) * cos(w) - sin(omega) * cos(w) * cos(i),
                    sin(omega) * sin(i),
                ],
                [
                    sin(omega) * cos(w) + cos(omega) * sin(w) * cos(i),
                    -sin(omega) * sin(w) + cos(omega) * cos(w) * cos(i),
                    -cos(omega) * sin(i),
                ],
                [sin(omega) * sin(i), cos(omega) * sin(i), cos(i)],
            ]
        )

    # TODO fix this
    def getGeocentricEquatorialCoordinates(self) -> GeocentricEquatorialCoordinates:
        vectorResult = np.matmul(
            self.transformationMatrix,
            self.getPerifocalCoordinates().getCoordinateVector(),
        )
        return GeocentricEquatorialCoordinates(
            vectorResult[0], vectorResult[1], vectorResult[2]
        )

    def inEclipse(self) -> bool:
        pass


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
