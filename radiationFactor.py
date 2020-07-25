import numpy, math
import scipy as sc
from scipy import integrate
from scipy.integrate import quad, dblquad, nquad
def radiationFunction(areai, thetai, thetaj, sD, areaj):
    #sD = shortestDist
    return cos(thetai)*cos(thetaj)/(Pi*sD*sD)

def bounds_i():
    return [0, areai]
def bounds_j():
    return [0, areaj]

radiationIntegral = integrate.nquad(radiationFunction, [bounds_i, bounds_j])

radiationFactor = 1/(areai) * radiationIntegral
print(radiationFactor)

radiationFunction(1, 2, 3, 4, 1)