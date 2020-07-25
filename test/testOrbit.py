import unittest

from constants import EARTH_RADIUS
from Orbit import Orbit
from OrbitalBody import EARTH_ORBITAL_BODY

inclination = 0.5
rightAscension = 0.75
argumentOfPeriapsis = 1.25
maxAltitude = pow(10, 6)
eccentricity = 0.1
orbit = Orbit(
    inclination,
    rightAscension,
    argumentOfPeriapsis,
    maxAltitude,
    eccentricity,
    EARTH_ORBITAL_BODY,
)


class TestOrbit(unittest.TestCase):
    def testSemiMajorAxis(self) -> None:
        semiMajorAxis = orbit.semiMajorAxis
        expected = (EARTH_RADIUS + maxAltitude) / (1 + eccentricity)
        self.assertAlmostEqual(expected, semiMajorAxis)

    def testEccentricAnomallyCoefficient(self) -> None:
        coefficient = orbit._getEccentricAnomalyCoefficient()
        expected = 868.824265503542
        self.assertAlmostEqual(expected, coefficient)

    def testEccentricAnomally(self) -> None:
        time = 1.4
        expected = 0.0017904
        eccentricAnomaly = orbit.getEccentricAnomaly(time)
        self.assertAlmostEqual(expected, eccentricAnomaly)


if __name__ == "__main__":
    unittest.main()
