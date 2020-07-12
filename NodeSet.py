from typing import List

import numpy as np

from Node import Node


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

    def getConductionRateMatrix(self) -> np.ndarray:
        conductionMatrix = np.zeros((self.numNodes, self.numNodes))
        for i in range(self.numNodes):
            for j in range(i):
                sendNode = self.nodes[i]
                receiveNode = self.nodes[j]
                contactConductance = self.contactConductanceMatrix[i][j]
                conduction = getConductionRate(
                    sendNode, receiveNode, contactConductance
                )
                conductionMatrix[i][j] = conduction
                conductionMatrix[j][i] = -conduction
        return conductionMatrix


def validateRadiationViewFactorMatrix(
    nodes: List[Node], radiationViewFactorMatrix: np.ndarray
) -> bool:  # TODO: Calculate radiation view factors using formulas
    surfaceAreas = list(map(lambda node: node.physicalProperties.surfaceArea, nodes))
    numNodes = len(nodes)
    for i in range(numNodes):
        for j in range(numNodes):
            energy1 = surfaceAreas[i] * radiationViewFactorMatrix[i][j]
            energy2 = surfaceAreas[j] * radiationViewFactorMatrix[j][i]
            if energy1 != energy2:
                return False
    return True


def getConductionRate(
    sendNode: Node, receiveNode: Node, contactConductance: float
) -> float:
    temperatureDifference = sendNode.temperature - receiveNode.temperature
    return contactConductance * temperatureDifference
