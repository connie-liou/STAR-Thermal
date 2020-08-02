import numpy as np
import math
import scipy as sc
from scipy import integrate
from scipy.integrate import quad, dblquad, nquad

import numpy as np


def integrateRadiationFactors(width_i, width_j, length_i, length_j, thetai, thetaj):
    def radiationFunction(thetai, thetaj, width_i, width_j):
        return (
            np.cos(thetai)
            * np.cos(thetaj)
            / (np.pi * ((width_i / 2) ** 2 + (width_j / 2) ** 2))
        )

    def bounds_lengthi():
        return [0, length_i]

    def bounds_widthi():
        return [0, width_i]

    def bounds_lengthj():
        return [0, length_j]

    def bounds_widthj():
        return [0, width_j]

    area_i = length_i * width_i

    radiationIntegral = integrate.nquad(
        radiationFunction,
        [bounds_lengthi, bounds_widthi, bounds_lengthj, bounds_widthj],
    )

    return 1 / (area_i) * radiationIntegral


# print(integrateRadiationFactors(1, 1, 1, 1, .5, .5))
