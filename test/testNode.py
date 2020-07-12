import unittest

from Node import Node
from OpticalProperties import OpticalProperties
from PhysicalProperties import PhysicalProperties

physicalProperties = PhysicalProperties(3, 4, 5, 6)
opticalProperties = OpticalProperties(0.3, 0.4)
node = Node("node1", physicalProperties, opticalProperties, 300)


class TestNode(unittest.TestCase):
    def testNodePhysicalProperties(self) -> None:
        self.assertEqual(physicalProperties, node.physicalProperties)

    def testNodeOpticalProperties(self) -> None:
        self.assertEqual(opticalProperties, node.opticalProperties)


if __name__ == "__main__":
    unittest.main()
