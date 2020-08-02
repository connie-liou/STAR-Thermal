import model.constants as constants


class OrbitalBody:
    def __init__(
        self,
        radius: float,
        gravitationalParamter: float,
        effectiveTemperature: float,
        albedo: float,
        solarConstant: float,
    ):
        self.radius = radius
        self.gravitationalParamter = gravitationalParamter
        self.effectiveTemperature = effectiveTemperature
        self.albedo = albedo
        self.solarConstant = solarConstant


EARTH_ORBITAL_BODY = OrbitalBody(
    constants.EARTH_RADIUS,
    constants.EARTH_GRAVITATIONAL_PARAMETER,
    constants.EARTH_EFFECTIVE_TEMPERATURE,
    constants.EARTH_ALBEDO,
    constants.EARTH_SOLAR_CONSTANT,
)
