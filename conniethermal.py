import numpy as np
import matplotlib.pyplot as plt


#calculating absorbed heat loads received from spacecraft

albedo = 0.3 #albedo of earth
Ssolar= 1373 #solar flux constant @ earth # W/m^2
Rearth= 6371000 #radius earth m
Searth= 236 # W/m^2
h = 500000#altitude of spacecraft m

#material prop
r=0.05 #10cm diameter
Area = np.pi*pow(r, 2) 
sArea = 4*np.pi*pow(r,2)
Vol = (4/3) * np.pi*pow(r, 3)

#http://homepages.cae.wisc.edu/~hessel/faqs/thermalPropertiesOfMetalsAndCoatings.htm
a = 0.65 #absorptivity i'm using black anodized aluminum
e = 0.85 #emissivity
csp = 880 # specific heat(J/kgK)
density = 3970
C= csp*density*Vol


# start at noon 
eclipseLength=30 #minutes
period = 90 #minutes
sunLength = period-eclipseLength

Qlist = [] #watts
Tlist = []
Temp = 273 #initial temp
time = [x for x in range(500)]
for i in time:
    orbitTime = i%90
    if ((orbitTime > sunLength/2) and (orbitTime < (sunLength/2)+eclipseLength)):
        #we are in eclipse
        Qtot = 0
        Qlist.append(Qtot)
        # delT = Qtot/C
        # Tlist.append(Temp + delT)
        
    else: 
        #we are in sunlight
        QSolarRad = a * Area * Ssolar
        QAlbedo = a*Ssolar * albedo * Area * (Rearth/ pow(Rearth+h, 2))
        QIR = e * Searth * Area * (Rearth/pow(Rearth+h, 2))

        Qtot = QSolarRad + QAlbedo + QIR 
        #delT = Qtot/C
        Qlist.append(Qtot)
  
plt.plot(time, Qlist)
plt.ylabel('Watts received')
plt.xlabel('Time (min)')
plt.show()