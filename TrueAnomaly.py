import math

def TrueAnomaly(
        eccentricity,
        eccentricAnomaly,
):
    cosTA = (eccentricity - cos(eccentricAnomaly)) / (eccentricity * cos(eccentricAnomaly) - 1) # eqn 2.25

    if eccentricAnomaly <= math.pi: # eqn 2.26
        trueAnomaly = acos(cosTA)
    else:
        trueAnomaly = 2 * math.pi - acos(cosTA)
