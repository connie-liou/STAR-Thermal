import numpy as np
import math
import scipy as sc
from scipy import integrate
from scipy.integrate import quad, dblquad, nquad

import numpy as np


def radiationFunction(thetai, thetaj, width_i, width_j):
     return cos(thetai)*cos(thetaj)/(np.pi*((width_i/2)**2+(width_j/2)**2))

def bounds_lengthi(length_i):
    return [0, length_i]
def bounds_widthi(width_i):
    return [0, width_i]

def bounds_lengthj(length_j):
    return [0, length_j]
def bounds_widthj(width_j):
    return [0, width_j]

def area_i(length_i, width_i):
    return length_i*width_i

radiationIntegral = integrate.nquad(radiationFunction, [bounds_lengthi, bounds_widthi, bounds_lengthj, bounds_widthj])

radiationFactor = 1/(area_i) * radiationIntegral


radiationFunction(2, 3, 4, 4)
bounds_lengthi(2)
bounds_widthi(3)
bounds_lengthj(4)
bounds_widthj(2)
area_i(2, 3)

print(radiationIntegral)
print(radiationFactor)

