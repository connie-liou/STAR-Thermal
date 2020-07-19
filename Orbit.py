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
