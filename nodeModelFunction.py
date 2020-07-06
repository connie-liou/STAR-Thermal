import matplotlib.pyplot as plt
import numpy as np
import NodeSet

def nodeModel(nodeSet: NodeSet, h, eclipseLength, period):
    #Inputs array of nodes, node adjacency matrix, node radiation view factors, spacecraft altitude, etc.

    nodeArray = nodeSet.nodes 
    nodeRadiationMatrix = nodeSet.radiationViewFactorMatrix 
    nodeConductanceMatrix = nodeSet.contactConductanceMatrix 
    numNodes = nodeSet.numNodes
    #constants
    albedo = 0.3  # albedo of earth
    solarFlux = 1373  # solar flux constant @ earth # W/m^2
    Rearth = 6371000  # radius earth m
    Searth = 236  # W/m^2
    stefanBoltzman = 5.67 * pow(10, -8)  # W/(m^2 K^4)

    sunLength = period - eclipseLength

    dQList = []  # watts
    totalHeatList = []  # joules
    totalChangeInHeat = 0
    Tlist = []

    time = [x for x in range(1000)]

    #find resistance matrices before loop
    #resistance for one surface
    res_self_mat_inv = [x for x in range(numNodes)]
    #resistances between surfaces
    res_other_mat_inv = [range(numNodes) for x in range(numNodes)] 
    for i in range(numNodes):
        res_self_mat_inv = nodeArray[i].opticalProperties.emissivity * nodeArray[i].physicalProperties.surfaceArea/(1-nodeArray[i].opticalProperties.emissivity)
        for j in range(numNodes): #1/Rij = A1 * Fij, skew symmetric matrix
            res_other_mat_inv = (nodeArray[i].physicalProperties.surfaceArea * nodeArray.radiationViewFactorMatrix[i][j])
    
    #J coefficient matrix eqn 2.19, like solving node-voltage analysis
    res_J_coeff = res_other_mat_inv
    for i in range(numNodes):
        for j in range(numNodes):
            if i==j: #fill diags with coeffs
                res_J_coeff = -(res_self_mat_inv[i] + np.sum(res_other_mat_inv[i]) )
    
    
    for i in time:
        orbitTime = i % period
        in_eclipse = (orbitTime > sunLength / 2) and (orbitTime < sunLength / 2 + eclipseLength)

        heightFactor = Rearth / pow(Rearth + h, 2)

        for n in range (len(nodeArray)):
            node = nodeArray[n]

            absorptivity = node.opticalProperties.absorptivity
            emissivity = node.opticalProperties.emissivity
            surfaceArea = node.physicalProperties.surfaceArea
            thickness = node.physicalProperties.thickness
            mass = node.physicalProperties.mass
            specificHeat = node.physicalProperties.specificHeat
            temperature = node.temperature


            #environmental inputs
            #consider sunpointing models, and how different sides get different amounts of sunlight? 
            #need radiation view factors wrt earth
            dQAlbedo = absorptivity * solarFlux * albedo * thickness * heightFactor
            dQIR = emissivity * Searth * thickness * heightFactor
            dQSolarRad = 0 if in_eclipse else absorptivity * thickness * solarFlux
            dQEmitted = emissivity * stefanBoltzman * surfaceArea * pow(temperature, 4)

            dQtot = dQAlbedo + dQIR + dQSolarRad - dQEmitted
            #dQList.append(dQtot) TODO: new plot for each node

            #TODO:conductance
            
            #radiation network, solve system for J values...
            #solve matrix of J coefficients eqn. 2.19
            Ematrix = []
            for x in range(numNodes):
                Ematrix.append (-(stefanBoltzman*emissivity*pow(temperature,4))*res_self_mat_inv[x])
            Jmatrix = np.linalg.solve(np.asarray(res_J_coeff), np.asarray(Ematrix))

            for y in range(numNodes):
                dQradiationNetwork += (Jmatrix[n]-Jmatrix[y])*(res_other_mat_inv[n][y])

            dQtot += dQradiationNetwork
            
            deltaQ = dQtot * 60
            totalChangeInHeat += deltaQ
            #totalHeatList.append(totalChangeInHeat)

            deltaTemp = deltaQ / (mass * specificHeat)

            node.temperature += deltaTemp
            #Tlist.append(currentTemp)