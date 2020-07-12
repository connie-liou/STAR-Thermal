import unittest

import numpy as np

from Node import Node
from NodeSet import NodeSet
from OpticalProperties import OpticalProperties
from PhysicalProperties import PhysicalProperties

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


class TestNodeSet(unittest.TestCase):
    def testConductionRateMatrix(self) -> None:
        expected = np.array([[0, 80], [-80, 0]])
        actual = nodeSet.getConductionRateMatrix()
        print(actual)
        self.assertTrue(np.array_equal(expected, nodeSet.getConductionRateMatrix()))


if __name__ == "__main__":
    unittest.main()
