import unittest

from Node import Node
from OpticalProperties import OpticalProperties
from PhysicalProperties import PhysicalProperties

startTemperature = 300
physicalProperties = PhysicalProperties(3, 4, 5, 6)
opticalProperties = OpticalProperties(0.3, 0.4)
node = Node("node1", physicalProperties, opticalProperties, startTemperature)


class TestNode(unittest.TestCase):
    def testNodePhysicalProperties(self) -> None:
        self.assertEqual(physicalProperties, node.physicalProperties)

    def testNodeOpticalProperties(self) -> None:
        self.assertEqual(opticalProperties, node.opticalProperties)

    def testBlackbodyEmissivePower(self) -> None:
        self.assertAlmostEqual(459.27, node.getBlackbodyEmissivePower())

    def testSurfaceResistance(self) -> None:
        self.assertAlmostEqual(0.5, node.getSurfaceResistance())


if __name__ == "__main__":
    unittest.main()
