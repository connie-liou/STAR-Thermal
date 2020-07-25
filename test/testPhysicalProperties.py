import unittest

from PhysicalProperties import PhysicalProperties


class TestPhysicalProperties(unittest.TestCase):
    def testCreatePhysicalProperties(self) -> None:
        physical = PhysicalProperties(1, 2, 3, 4)
        self.assertEqual(1, physical.surfaceArea)
        self.assertEqual(2, physical.thickness)
        self.assertEqual(3, physical.density)
        self.assertEqual(4, physical.specificHeat)

    def testVolume(self) -> None:
        physical = PhysicalProperties(5, 2, 3, 4)
        self.assertEqual(10, physical.volume)

    def testMass(self) -> None:
        physical = PhysicalProperties(5, 2, 3, 4)
        self.assertEqual(30, physical.mass)


if __name__ == "__main__":
    unittest.main()
