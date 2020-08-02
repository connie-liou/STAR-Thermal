import numpy as np

from model.constants import STEFAN_BOLTZMAN
from model.components.opticalProperties import OpticalProperties
from model.components.physicalProperties import PhysicalProperties


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
        return STEFAN_BOLTZMAN * pow(self.temperature, 4)

    def getSurfaceResistance(self) -> float:
        emissivity = self.opticalProperties.emissivity
        surfaceArea = self.physicalProperties.surfaceArea
        return (1 - emissivity) / (surfaceArea * emissivity)
