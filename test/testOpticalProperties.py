import unittest

from OpticalProperties import OpticalProperties


class TestOpticalProperties(unittest.TestCase):
    def testOpticalProperties(self) -> None:
        optical = OpticalProperties(0.1, 0.2)
        self.assertEqual(0.1, optical.absorptivity)
        self.assertEqual(0.2, optical.emissivity)


if __name__ == "__main__":
    unittest.main()
