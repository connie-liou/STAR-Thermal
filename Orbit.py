class Orbit:
    def __init__(
        self,
        inclination: float,
        rightAscensionOfAscendingNode: float,
        argumentOfPeriapsis: float,
        maxAltitude: float,
        eccentricity: float,
    ):
        self.inclination = inclination
        self.rightAscensionOfAscendingNode = rightAscensionOfAscendingNode
        self.argumentOfPeriapsis = argumentOfPeriapsis
        self.maxAltitude = maxAltitude
        self.eccentricity = eccentricity
