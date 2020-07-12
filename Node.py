import numpy as np

from OpticalProperties import OpticalProperties
from PhysicalProperties import PhysicalProperties


class Node:
    def __init__(
        self,
        name: str,
        physicalProperties: PhysicalProperties,
        opticalProperties: OpticalProperties,
        initialTemperature: float,
    ):
        self.name = name
        self.physicalProperties = physicalProperties
        self.opticalProperties = opticalProperties
        self.temperature = initialTemperature

    def getBlackbodyEmissivePower(self) -> float:
        stefanBoltzman: float = 5.67 * pow(10, -8)
        return stefanBoltzman * pow(self.temperature, 4)

    def getSurfaceResistance(self) -> float:
        emissivity = self.opticalProperties.emissivity
        surfaceArea = self.physicalProperties.surfaceArea
        return (1 - emissivity) / (surfaceArea * emissivity)
