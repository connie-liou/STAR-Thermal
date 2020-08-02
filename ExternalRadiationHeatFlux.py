import numpy as np

def ExternalRadiationHeatFlux(
        solarAbsorptivity,
        psi, # angle between the surface normal vector and the direction of the solar rays
        Te, # effective blackbody temperature of Earth, 255K on average
        alphaIR, # IR absorptivity of the material
        Fe, # view factor from the spacecraft surface to the Earth's disk (from sect. 2.1.3)
        AF, # albedo factor, fraction of solar radiation that is reflected off Earth's atmosphere, ranges 0.18-0.55
        theta, # angle between solar rays and position vector of surface
):
    # constants:
    Gs = 1367 # solar constant Gs = 1367 W/m^2 on average
    sigma = 5.67 * pow(10, -8)  # stefan boltzmann constant [W / (m^2 K^4)]

    qs = Gs * solarAbsorptivity * np.cos(psi) # eqn 2.31, direct solar radiation flux absorbed by a spacecraft surface
    qe = sigma * pow(Te, 4) * alphaIR * Fe # eqn 2.32, direct Earth IR radiation flux absorbed by spacecraft surface
    if theta < (np.pi / 2):
        qa = Gs * AF * solarAbsorptivity * Fe * np.cos(theta) # eqn 2.33, albedo radiation flux absorbed by spacecraft surface
    else:
        qa = 0 # eqn. 2.34, receiving small amt of albedo radiation

    qext = qs + qe + qa # eqn 2.35, total external radiation heat flux absorbed by spacecraft surface
    return qext