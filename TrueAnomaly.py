import math


def TrueAnomaly(
        eccentricity,
        eccentricAnomaly,
):
    cosTA = (eccentricity - math.cos(eccentricAnomaly)) / (eccentricity * math.cos(eccentricAnomaly) - 1) # eqn 2.25

    if eccentricAnomaly <= math.pi: # eqn 2.26
        return math.acos(cosTA)
    else:
        return 2 * math.pi - math.acos(cosTA)
