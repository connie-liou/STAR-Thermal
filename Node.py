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
