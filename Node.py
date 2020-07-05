import numpy as np

class Node:
    def __init__(self, name, physicalProperties, opticalProperties, initialTemperature):
        self.name = name
        self.physicalProperties = physicalProperties
        self.opticalProperties = opticalProperties
        self.temperature = initialTemperature
    
