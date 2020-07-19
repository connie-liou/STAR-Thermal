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
    def testConductionHeatTransferRateMatrix(self) -> None:
        expected = np.array([[0, 80], [-80, 0]])
        actual = nodeSet.getConductionHeatTransferRateMatrix()
        self.assertTrue(np.array_equal(expected, actual))

    def testSpaceResistance(self) -> None:
        expected = 1 / (3 * 0.2)
        actual = nodeSet.getSpaceResistance(0, 1)
        self.assertEqual(expected, actual)

    def testConductionHeatTransferRates(self) -> None:
        expected = np.array([-80, 80])
        actual = nodeSet.getConductionHeatTransferRates()
        self.assertTrue(np.array_equal(expected, actual))

    def testRadiationHeatTransferSystemCoefficientsSingleNode0(self) -> None:
        """This test assumes that node.getSurfaceResistance and
        nodeSet.getSpaceResistance work properly.    
        """
        expected = np.array(
            [
                -1 / node0.getSurfaceResistance()
                - 1 / nodeSet.getSpaceResistance(0, 1),
                1 / nodeSet.getSpaceResistance(0, 1),
            ]
        )
        actual = nodeSet._getRadiationHeatTransferSystemCoefficientsSingleNode(0)
        self.assertTrue(np.array_equal(expected, actual))

    def testRadiationHeatTransferSystemCoefficientsSingleNode1(self) -> None:
        """This test assumes that node.getSurfaceResistance and
        nodeSet.getSpaceResistance work properly.    
        """
        expected = np.array(
            [
                1 / nodeSet.getSpaceResistance(1, 0),
                -1 / node1.getSurfaceResistance()
                - 1 / nodeSet.getSpaceResistance(1, 0),
            ]
        )
        actual = nodeSet._getRadiationHeatTransferSystemCoefficientsSingleNode(1)
        self.assertTrue(np.array_equal(expected, actual))

    def testRadiationHeatTransferSystemCoefficients(self) -> None:
        """This test assumes that node.getSurfaceResistance and
        nodeSet.getSpaceResistance work properly.    
        """
        expected = np.array(
            [
                [
                    -1 / node0.getSurfaceResistance()
                    - 1 / nodeSet.getSpaceResistance(0, 1),
                    1 / nodeSet.getSpaceResistance(0, 1),
                ],
                [
                    1 / nodeSet.getSpaceResistance(1, 0),
                    -1 / node1.getSurfaceResistance()
                    - 1 / nodeSet.getSpaceResistance(1, 0),
                ],
            ]
        )
        actual = nodeSet._getRadiationHeatTransferSystemCoefficients()
        self.assertTrue(np.array_equal(expected, actual))

    def testRadiationHeatTransferSystemDependentVariables(self) -> None:
        """This test assumes that node.getSurfaceResistance and
        node.getBlackBodyEmissivePower work properly.    
        """
        power0 = node0.getBlackbodyEmissivePower()
        resistance0 = node0.getSurfaceResistance()
        power1 = node1.getBlackbodyEmissivePower()
        resistance1 = node1.getSurfaceResistance()
        expected = np.array([-power0 / resistance0, -power1 / resistance1])
        actual = nodeSet._getRadiationHeatTransferSystemDependentVariables()
        self.assertTrue(np.array_equal(actual, expected))

    def testRadiationHeatTransferRateMatrix(self) -> None:
        """This test assumes that the functions to get the
        coefficients and dependent variables work correctly.
        """
        expected = np.array([357.9338298, 20.14659574])
        actual = nodeSet.getRadiationHeatTransferRates()
        self.assertTrue(np.allclose(expected, actual))


if __name__ == "__main__":
    unittest.main()
