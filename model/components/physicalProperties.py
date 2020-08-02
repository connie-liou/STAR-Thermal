class PhysicalProperties:
    def __init__(
        self, surfaceArea: float, thickness: float, density: float, specificHeat: float
    ):
        self.surfaceArea = surfaceArea
        self.thickness = thickness
        self.density = density
        self.specificHeat = specificHeat
        self.volume = surfaceArea * thickness
        self.mass = self.volume * density
