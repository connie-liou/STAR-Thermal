from math import cos, pi

from model.constants import STEFAN_BOLTZMAN


# TODO check if satellite is in eclipse

# TODO is IR absorptivity the same as solar absorptivity?
def solarRadiationFlux(
        solarConstant: float, absorptivitySolar: float, angleNormalToRays: float
) -> float:
    """The angle is between the normal vector to the surface and the
    direction of the solar rays hitting the surface.
    """
    return solarConstant * absorptivitySolar * cos(angleNormalToRays)


def orbitalBodyIRFlux(
        effectiveBlackbodyTemp: float, absorptivityIR: float, viewFactor: float
) -> float:
    return STEFAN_BOLTZMAN * pow(effectiveBlackbodyTemp, 4) * absorptivityIR * viewFactor


def albedoRadiationFlux(
        solarConstant: float,
        albedoFactor: float,
        absorptivitySolar: float,
        viewFactor: float,
        anglePositionVectorToRays: float,
) -> float:
    """The angle is between solar rays and the position vector of the
    satellite's surface
    """
    if anglePositionVectorToRays < pi / 2:
        return solarConstant * albedoFactor * absorptivitySolar * viewFactor * cos(anglePositionVectorToRays)
    return 0
