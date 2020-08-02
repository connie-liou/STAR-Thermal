import unittest

from model.constants import EARTH_RADIUS
from model.components.orbit import Orbit
from model.components.orbitalBody import EARTH_ORBITAL_BODY

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

    def testEccentricAnomalyCoefficient(self) -> None:
        coefficient = orbit._getEccentricAnomalyCoefficient()
        expected = 868.824265503542
        self.assertAlmostEqual(expected, coefficient)

    def testEccentricAnomaly(self) -> None:
        time = 1.4
        expected = 0.0017904
        eccentricAnomaly = orbit.getEccentricAnomaly(time)
        self.assertAlmostEqual(expected, eccentricAnomaly)

    # TODO write test once function is written
    def testTrueAnomaly(self) -> None:
        self.assertTrue(False)

    def testDistanceFromOrbitalBody(self) -> None:
        expected = 2
        distance = orbit.getDistanceFromOrbitalBody(0.002)
        self.assertAlmostEqual(expected, distance)


if __name__ == "__main__":
    unittest.main()
