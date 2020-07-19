from NodeSet import NodeSet
from Orbit import Orbit
from OrbitalBody import OrbitalBody
from Orientation import Orientation
from SolarPosition import SolarPosition
from SpacecraftConfiguration import SpacecraftConfiguration
from TimeConfiguration import TimeConfiguration


class ThermalModel:
    def __init__(
        self,
        timeConfiguration: TimeConfiguration,
        spacecraftConfiguration: SpacecraftConfiguration,
        orbit: Orbit,
        orientation: Orientation,
        orbitalBody: OrbitalBody,
        solarPosition: SolarPosition,
        nodes: NodeSet,
    ):
        self.timeConfiguration = timeConfiguration
        self.spacecraftConfiguration = SpacecraftConfiguration
        self.orbit = Orbit
        self.orientation = orientation
        self.orbitalBody = OrbitalBody
        self.solarPosition = SolarPosition
        self.nodes = NodeSet

    def simulate(self) -> None:
        raise NotImplementedError
