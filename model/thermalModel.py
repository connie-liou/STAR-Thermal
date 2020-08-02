from model.components.nodeSet import NodeSet
from model.components.orbit import Orbit
from model.components.orbitalBody import OrbitalBody
from model.components.orientation import Orientation
from model.components.solarPosition import SolarPosition
from model.components.spacecraftConfiguration import SpacecraftConfiguration
from model.components.timingConfiguration import TimingConfiguration


class ThermalModel:
    def __init__(
        self,
        timeConfiguration: TimingConfiguration,
        spacecraftConfiguration: SpacecraftConfiguration,
        orbit: Orbit,
        orientation: Orientation,
        solarPosition: SolarPosition,
        nodes: NodeSet,
    ):
        self.timeConfiguration = timeConfiguration
        self.spacecraftConfiguration = SpacecraftConfiguration
        self.orbit = Orbit
        self.orientation = orientation
        self.solarPosition = SolarPosition
        self.nodes = NodeSet

    def simulate(self) -> None:
        raise NotImplementedError
