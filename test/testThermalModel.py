import unittest
import numpy as np

from model.components.node import Node
from model.components.nodeSet import NodeSet
from model.components.opticalProperties import OpticalProperties
from model.components.orbit import Orbit
from model.components.physicalProperties import PhysicalProperties
from model.components.spacecraftConfiguration import SpacecraftConfiguration
from model.components.timingConfiguration import TimingConfiguration
from model.thermalModel import ThermalModel

timingConfig = TimingConfiguration(100, 1)
spacecraftConfig = SpacecraftConfiguration.RECTANGLE
orbit = None
orientation = None
solarPosition = None

startTemperature0 = 300
physicalProperties0 = PhysicalProperties(3, 4, 5, 6)
opticalProperties0 = OpticalProperties(0.3, 0.4)
node0 = Node("node0", physicalProperties0, opticalProperties0, startTemperature0)

startTemperature1 = 100
physicalProperties1 = PhysicalProperties(6, 8, 9, 10)
opticalProperties1 = OpticalProperties(0.1, 0.7)
node1 = Node("node1", physicalProperties1, opticalProperties1, startTemperature1)

nodeList = [node0, node1]

radiationViewFactorsMatrix = np.array([[0, 0.2], [0.1, 0]])

contactConductanceMatrix = np.array([[0, 0.4], [0.4, 0]])

nodeSet = NodeSet(nodeList, radiationViewFactorsMatrix, contactConductanceMatrix)

thermalModel = ThermalModel(
    timingConfig,
    spacecraftConfig,
    orbit,
    orientation,
    solarPosition,
    nodeSet
)


class TestThermalModel(unittest.TestCase):
    def testSimulation(self) -> None:
        print("testSimulation")
        results = thermalModel.simulate()
        print("RESULTS")
        print(results)


if __name__ == "__main__":
    unittest.main()
