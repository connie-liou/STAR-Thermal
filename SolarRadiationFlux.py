import numpy as np

def SolarRadiationFlux(
        solarAbsorptivity,
        psi, # angle between the surface normal vector and the direction of the solar rays
):
    Gs = 1367 # solar constant Gs = 1367 W/m^2 on average
    qs = Gs * solarAbsorptivity * np.cos(psi) # eqn 2.31, direct solar radiation flux absorbed by a spacecraft surface
    return qs