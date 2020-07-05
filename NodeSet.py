class NodeSet:
    def __init__(self, nodes, radiationViewFactorMatrix, contactConductanceMatrix):
        self.nodes = nodes
        self.radiationViewFactorMatrix = radiationViewFactorMatrix
        self.contactConductanceMatrix = contactConductanceMatrix
        self.numNodes = len(nodes)

