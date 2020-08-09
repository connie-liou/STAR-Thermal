import numpy as np
import math

# determine if cubesat is in eclipse
# Re = radius of Earth in m
Re = 6371000


def inEclipse(scx, scy, scz, sx, sy, sz):
    # find magnitude of spacecraft position vector
    # vector found from previous file code 2.2.1
    SpacecraftPosition = np.array([scx, scy, scz])
    Rsc = np.linalg.norm(SpacecraftPosition)
    print('Rsc', Rsc)

    # find magnitude of sun position vector
    SunPosition = np.array([sx, sy, sz])
    Rs = np.linalg.norm(SunPosition)
    print('Rs', Rs)

    # calculate the two angles that define the transition point from sun to shade
    input1 = Re / Rsc
    input2 = Re / Rs

    theta1 = math.acos(input1)
    theta2 = math.acos(input2)

    thetaTotal = theta1 + theta2

    # calculate the angle between the spacecraft's actual position vector and the sun's position vector
    thetaActual = math.acos((np.dot(SpacecraftPosition, SunPosition)) / (Rsc * Rs))

    print(f'thetaActual = {thetaActual}, thetaTotal: {thetaTotal}')

    return thetaActual > thetaTotal
