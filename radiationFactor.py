import numpy, math
import scipy as sc
from scipy import integrate
from scipy.integrate import quad, dblquad, nquad
def radiationFunction(thetai, thetaj, sD):
    #sD = shortest distance
    return cos(thetai)*cos(thetaj)/(Pi*sD*sD)

def bounds_i(areai):
    return [0, areai]
def bounds_j(areaj):
    return [0, areaj]

radiationIntegral = integrate.nquad(radiationFunction, [bounds_i, bounds_j])

radiationFactor = 1/(areai) * radiationIntegral
print(radiationFactor)

radiationFunction(2, 3, 4)
bounds_i(1)
bounds_j(1)