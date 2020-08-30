from typing import List

import numpy as np
import matplotlib.pyplot as plt

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
        self.spacecraftConfiguration = spacecraftConfiguration
        self.orbit = orbit
        self.orientation = orientation
        self.solarPosition = solarPosition
        self.nodeSet = nodeSet

    def getHeatTransferRates(self) -> np.array:
        # # Internal heat transfer
        # conductionRates = self.nodeSet.getConductionHeatTransferRates()
        # internalRadiationRates = self.nodeSet.getRadiationHeatTransferRates()
        # # TODO Environmental heat transfer is not included yet
        #
        # return conductionRates + internalRadiationRates
        return [1 for node in self.nodeSet.nodes]

    def simulate(self) -> List[List[float]]:
        endTime = self.timingConfiguration.endTime
        timeStep = self.timingConfiguration.timeStep

        nodeTemperatures = []
        for node in self.nodeSet.nodes:
            nodeTemperatures.append([node.temperature])
        print(f'nodeTemperatures: {nodeTemperatures}')
        for _ in range(0, endTime, timeStep):
            heatTransferRates = self.getHeatTransferRates()
            changesInTemperature = np.zeros(self.nodeSet.numNodes)
            for index, node in enumerate(self.nodeSet.nodes):
                changesInTemperature[index] = (
                        heatTransferRates[index] / node.physicalProperties.thermalMass
                )
            previousTemperatures = []
            for singleNodeTemps in nodeTemperatures:
                previousTemperatures.append(singleNodeTemps[-1])
            print(f'previousTemperatures: {previousTemperatures}')
            for index, change in enumerate(changesInTemperature):
                newTemp = previousTemperatures[index] + change
                print(f'newTemp: {newTemp}')
                nodeTemperatures[index].append(newTemp)
            print(f'nodeTemperatures: {nodeTemperatures}')

        return nodeTemperatures
