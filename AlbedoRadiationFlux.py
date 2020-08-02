import numpy as np

def AlbedoRadiationFlux(
        AF, # albedo factor, fraction of solar radiation that is reflected off Earth's atmosphere, ranges 0.18-0.55
        solarAbsorptivity,
        Fe, # view factor from spacecraft surface to Earth's disk
        theta, # angle between solar rays and position vector of surface
):
    Gs = 1367  # solar constant Gs = 1367 W/m^2 on average

    if theta < (np.pi / 2):
        qa = Gs * AF * solarAbsorptivity * Fe * np.cos(theta) # eqn 2.33
    else:
        qa = 0 # eqn. 2.34, receiving small amt of albedo radiation

    return qa