class OrbitalBody:
    def __init__(
        self,
        radius: float,
        gravitationalParamter: float,
        effectiveBlackbodyTemperature: float,
        albedo: float,
        solarConstant: float,
    ):
        self.radius = radius
        self.gravitationalParamter = (gravitationalParamter,)
        self.effectiveBlackbodyTemperature = (effectiveBlackbodyTemperature,)
        self.albedo = (albedo,)
        self.solarConstant = solarConstant
