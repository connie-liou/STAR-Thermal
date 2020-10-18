import matplotlib.pyplot as plt
import numpy as np

from model.constants import STEFAN_BOLTZMAN


# calculating absorbed heat loads received from spacecraft
def ThermalFunction(
    h,
    r,
    emissivity,
    absorptivity,
    specificHeat,
    density,
    startTemp,
    eclipseLength,
    period,
):

    albedo = 0.3  # albedo of earth
    solarFlux = 1373  # solar flux constant @ earth # W/m^2
    Rearth = 6371000  # radius earth m
    Searth = 236  # W/m^2
    # h = 500000  # altitude of spacecraft m

    # material prop
    # r = 0.05  # 10cm diameter
    crossSectionalArea = np.pi * pow(r, 2)
    surfaceArea = 4 * np.pi * pow(r, 2)
    volume = (4 / 3) * np.pi * pow(r, 3)

    # http://homepages.cae.wisc.edu/~hessel/faqs/thermalPropertiesOfMetalsAndCoatings.htm
    # absorptivity = 0.65  # absorptivity i'm using black anodized aluminum
    # emissivity = 0.85  # emissivity
    # specificHeat = 880  # specific heat(J/kgK)
    # density = 3970
    mass = density * volume

    # start at noon
    # eclipseLength = 30  # minutes
    # period = 90  # minutes
    sunLength = period - eclipseLength

    dQList = []  # watts
    totalHeatList = []  # joules
    totalChangeInHeat = 0
    Tlist = []
    # startTemp = 273
    currentTemp = startTemp  # initial temp
    time = [x for x in range(1000)]
    for i in time:
        orbitTime = i % period
        in_eclipse = (orbitTime > sunLength / 2) and (
            orbitTime < sunLength / 2 + eclipseLength
        )

        heightFactor = Rearth / pow(Rearth + h, 2)

        dQIR = emissivity * Searth * crossSectionalArea * heightFactor
        # There is no albedo when the satellite in is eclipse
        dQAlbedo = (
            0
            if in_eclipse
            else absorptivity * solarFlux * albedo * crossSectionalArea * heightFactor
        )
        dQSolarRad = 0 if in_eclipse else absorptivity * crossSectionalArea * solarFlux
        dQEmitted = emissivity * STEFAN_BOLTZMAN * surfaceArea * pow(currentTemp, 4)

        dQtot = dQAlbedo + dQIR + dQSolarRad - dQEmitted
        dQList.append(dQtot)

        deltaQ = dQtot * 60
        totalChangeInHeat += deltaQ
        totalHeatList.append(totalChangeInHeat)

        deltaTemp = deltaQ / (mass * specificHeat)

        currentTemp += deltaTemp
        Tlist.append(currentTemp)

    plt.figure(1)
    plt.plot(time, dQList)
    plt.title("Derivative of Heat With Respect to Time")
    plt.ylabel("Watts received")
    plt.xlabel("Time (min)")

    plt.figure(2)
    plt.plot(time, totalHeatList)
    plt.title("Total Heat Received")
    plt.ylabel("Joules received")
    plt.xlabel("Time (min)")

    plt.figure(3)
    plt.plot(time, Tlist)
    plt.title("Temperature Over Time")
    plt.ylabel("Temperature")
    plt.xlabel("Time (min)")

    plt.show()


ThermalFunction(418500, 0.05, .85, .65, 880, 3970, 273, 35, 92.68)
