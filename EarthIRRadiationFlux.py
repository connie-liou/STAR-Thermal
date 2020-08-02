def EarthIRRadiationFlux( # ranges from 218-275 W/m^2
        Te, # effective blackbody temperature of Earth, 255K on average
        alphaIR, # IR absorptivity of the material
        Fe, # view factor from the spacecraft surface to the Earth's disk (from sect. 2.1.3)
):
    sigma = 5.67 * pow(10, -8)  # stefan boltzmann constant [W / (m^2 K^4)]
    qe = sigma * pow(Te, 4) * alphaIR * Fe # eqn 2.32, direct Earth IR radiation flux absorbed by spacecraft surface
    return qe