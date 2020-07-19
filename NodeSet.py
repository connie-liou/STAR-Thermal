from typing import List

import numpy as np

from Node import Node


# TODO: Calculate radiation view factors using formulas
class NodeSet:
    def __init__(
        self,
        nodes: List[Node],
        radiationViewFactorMatrix: np.ndarray,
        contactConductanceMatrix: np.ndarray,
    ) -> None:
        self.nodes = nodes
        self.radiationViewFactorMatrix = radiationViewFactorMatrix
        self.contactConductanceMatrix = contactConductanceMatrix
        self.numNodes = len(nodes)

    def getSpaceResistance(self, sendNodeIndex: int, receiveNodeIndex: int) -> float:
        sendNode = self.nodes[sendNodeIndex]
        receiveNode = self.nodes[receiveNodeIndex]
        viewFactor = self.radiationViewFactorMatrix[sendNodeIndex][receiveNodeIndex]
        return _getSpaceResistance(sendNode, receiveNode, viewFactor)

    def _getRadiationHeatTransferSystemCoefficientsSingleNode(
        self, nodeIndex: int
    ) -> np.array:
        node = self.nodes[nodeIndex]
        result = np.zeros(self.numNodes)
        result[nodeIndex] = -1 / node.getSurfaceResistance()
        for j in range(self.numNodes):
            spaceResistance = self.getSpaceResistance(nodeIndex, j)
            result[j] += 1 / spaceResistance
            result[nodeIndex] -= 1 / spaceResistance
        return result

    def _getRadiationHeatTransferSystemCoefficients(self) -> np.ndarray:
        coefficients = []
        for nodeIndex in range(self.numNodes):
            coefficients.append(
                self._getRadiationHeatTransferSystemCoefficientsSingleNode(nodeIndex)
            )
        return np.array(coefficients)

    def _getRadiationHeatTransferSystemDependentVariables(self) -> np.array:
        return np.array(
            list(map(_getRadiationHeatTransferSystemDependentVariable, self.nodes))
        )

    def getRadiationHeatTransferRates(self) -> np.ndarray:
        coefficients = self._getRadiationHeatTransferSystemCoefficients()
        dependentVariables = self._getRadiationHeatTransferSystemDependentVariables()
        return np.linalg.solve(coefficients, dependentVariables)

    def getConductionHeatTransferRateMatrix(self) -> np.ndarray:
        conductionMatrix = np.zeros((self.numNodes, self.numNodes))
        for i in range(self.numNodes):
            for j in range(i):
                sendNode = self.nodes[i]
                receiveNode = self.nodes[j]
                contactConductance = self.contactConductanceMatrix[i][j]
                conduction = _getConductionRate(
                    sendNode, receiveNode, contactConductance
                )
                conductionMatrix[i][j] = conduction
                conductionMatrix[j][i] = -conduction
        return conductionMatrix

    def getConductionHeatTransferRates(self) -> np.array:
        return self.getConductionHeatTransferRateMatrix().sum(axis=0)


def validateRadiationViewFactorMatrix(
    nodes: List[Node], radiationViewFactorMatrix: np.ndarray
) -> bool:
    surfaceAreas = list(map(lambda node: node.physicalProperties.surfaceArea, nodes))
    numNodes = len(nodes)
    for i in range(numNodes):
        for j in range(numNodes):
            energy1 = surfaceAreas[i] * radiationViewFactorMatrix[i][j]
            energy2 = surfaceAreas[j] * radiationViewFactorMatrix[j][i]
            if energy1 != energy2:
                return False
    return True


def _getConductionRate(
    sendNode: Node, receiveNode: Node, contactConductance: float
) -> float:
    temperatureDifference = sendNode.temperature - receiveNode.temperature
    return contactConductance * temperatureDifference


def _getSpaceResistance(sendNode: Node, receiveNode: Node, viewFactor: float) -> float:
    return 1 / (sendNode.physicalProperties.surfaceArea * viewFactor)


def _getRadiationHeatTransferSystemDependentVariable(node: Node) -> float:
    return -node.getBlackbodyEmissivePower() / node.getSurfaceResistance()
