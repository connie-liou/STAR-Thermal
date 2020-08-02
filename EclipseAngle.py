import numpy as np
import math

#determine if cubesat is in eclipse
#Re = radius of Earth in m
Re = 6371000

#find magnitude of spacecraft position vector
#vector found from previous file code 2.2.1
SpacecraftPosition = np.array([scx, scy, scz])
Rsc = np.linalg.norm(SpacecraftPosition)
print('Rsc', Rsc)

#find magnitude of sun position vector
SunPosition = np.array([sx, sy, sz])
Rs = np.linalg.norm(SunPosition)
print('Rs', Rs)

#calculate the two angles that define the transition point from sun to shade
angle1 = Re/Rsc
angle2 = Re/Rs

theta1 = math.acos(angle1)
theta2 = math.acos(angle2)

thetaTotal = theta1 + theta2

#calculate the angle between the spacecraft's actual position vector and the sun's position vector
thetaActual = math.acos((np.dot(SpacecraftPosition, SunPosition))/(Rsc*Rs))
print(thetaTotal, thetaActual)


if thetaActual < thetaTotal:
    print('line of sight does exist and the spacecraft is in sunlight')
else:
    print('there is no line of sight between the Sun and the spacecraft and the spacecraft is in eclipse')