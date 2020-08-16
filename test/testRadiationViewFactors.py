import unittest

from model.radiationViewFactors import RadiationViewFactors


class TestRadiationViewFactors(unittest.TestCase):
    def testParallelSquarePlates(self):
        expected = 0.1998
        actual = RadiationViewFactors.parallelSquarePlates(10, 10)
        self.assertAlmostEqual(expected, actual, 4)


if __name__ == '__main__':
    unittest.main()
