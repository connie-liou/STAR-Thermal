import numpy as np
import Node 

class NodeSet:
    def __init__(self, nodes, radiationViewFactorMatrix, contactConductanceMatrix):
        self.nodes = nodes #array of Nodes i'm assuming
        self.radiationViewFactorMatrix = radiationViewFactorMatrix
        self.contactConductanceMatrix = contactConductanceMatrix
        self.numNodes = len(nodes)

    def getConductionRateMatrix(self):
        conductionMatrix = np.zeros((self.numNodes, self.numNodes))
        for i in range(self.numNodes):
            for j in range(i):
                sendNode = self.nodes[i]
                receiveNode = self.nodes[j]
                contactConductance = self.contactConductanceMatrix[i][j]
                conduction = getConductionRate(sendNode, receiveNode, contactConductance)
                conductionMatrix[i][j] = conduction
                conductionMatrix[j][i] = -conduction
        return conductionMatrix

def validateRadiationViewFactorMatrix(nodes, radiationViewFactorMatrix): #TODO: Calculate radiation view factors using formulas
    surfaceAreas = list(map(lambda node: node.physicalProperties.surfaceArea, nodes))
    numNodes = len(nodes)
    for i in range(numNodes):
        for j in range(numNodes):
            energy1 = surfaceAreas[i] * radiationViewFactorMatrix[i][j]
            energy2 = surfaceAreas[j] * radiationViewFactorMatrix[j][i]
            if (energy1 != energy2):
                return False
    return True


def getConductionRate(sendNode, receiveNode, contactConductance):
    temperatureDifference = sendNode.temperature - receiveNode.temperature
    return contactConductance * temperatureDifference

