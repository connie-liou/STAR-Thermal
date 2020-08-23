import numpy as np

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
        timingConfiguration: TimingConfiguration,
        spacecraftConfiguration: SpacecraftConfiguration,
        orbit: Orbit,
        orientation: Orientation,
        solarPosition: SolarPosition,
        nodeSet: NodeSet,
    ):
        self.timingConfiguration = timingConfiguration
        self.spacecraftConfiguration = SpacecraftConfiguration
        self.orbit = Orbit
        self.orientation = orientation
        self.solarPosition = SolarPosition
        self.nodeSet = nodeSet

    def getHeatTransferRates(self) -> np.array:
        # Internal heat transfer
        conductionRates = self.nodeSet.getConductionHeatTransferRates()
        internalRadiationRates = self.nodeSet.getRadiationHeatTransferRates()
        # TODO Environmental heat transfer is not included yet

        return conductionRates + internalRadiationRates

    def simulate(self) -> None:
        currentTime = 0
        endTime = self.timingConfiguration.endTime
        timeStep = self.timingConfiguration.timeStep

        while currentTime < endTime:
            heatTransferRates = self.getHeatTransferRates()
            changesInTemperature = np.zeros(self.nodeSet.numNodes)
            for index, node in enumerate(self.nodeSet.nodes):
                changesInTemperature[index] = (
                    heatTransferRates[index] / node.physicalProperties.thermalMass
                )

            # TODO plot things
