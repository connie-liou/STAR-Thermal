import numpy as np
import matplotlib.pyplot as plt


#calculating absorbed heat loads received from spacecraft

albedo = 0.34 #albedo of earth
Ssolar= 1373 #solar flux constant @ earth # W/m^2, worst case 1418
Rearth= 6371000 #radius earth m
Searth= 236 # W/m^2
h = 500000 #altitude of spacecraft m

#material prop
r=0.05 #10cm diameter
Area = np.pi*pow(r, 2) 
sArea = 4*np.pi*pow(r,2)
Vol = (4/3) * np.pi*pow(r, 3)

#http://homepages.cae.wisc.edu/~hessel/faqs/thermalPropertiesOfMetalsAndCoatings.htm
a = 0.65 #absorptivity i'm using black anodized aluminum
e = 0.85 #emissivity
sigma = 5.67 * pow(10,(-8)) #stefan boltzman constant W/m^2K^4
csp = 880 # specific heat(J/kgK)
density = 3970
C= csp*density*Vol


# start at noon 
eclipseLength=0 #minutes
period = 90 #minutes
sunLength = period-eclipseLength

Qlist = [] #watts
Tlist = []
bodyTemp = 200 #initial temp

time = [x for x in range(3000)]
for i in time:
    orbitTime = i%90
    if ((orbitTime > sunLength/2) and (orbitTime < (sunLength/2)+eclipseLength)):
        #we are in eclipse

        #calculate energy received
        QIR = e * Searth * Area * (Rearth/pow(Rearth+h, 2))
        Qintot = QIR
        Qlist.append(Qintot)

        #calculate energy outputted by blackbody radiation
        delQout = e * sigma * sArea * pow((bodyTemp),4)
        #calculate deltaT based on total Q
        delT = 60*(Qintot-(delQout))/C
        
        bodyTemp = bodyTemp + delT
        Tlist.append(bodyTemp)
       # print(bodyTemp, delT, 'eclipse')
        
    else: 
        #we are in sunlight
        QSolarRad = a * Area * Ssolar
        QAlbedo = a*Ssolar * albedo * Area * (Rearth/ pow(Rearth+h, 2))
        QIR = e * Searth * Area * (Rearth/pow(Rearth+h, 2))
        Qintot = QSolarRad + QAlbedo + QIR 
        Qlist.append(Qintot)

        delQout = e * sigma * sArea * pow((bodyTemp),4)
        delT = 60*(Qintot-(delQout))/C
        
        bodyTemp = bodyTemp + delT
        Tlist.append(bodyTemp)
        #print(bodyTemp,Q, delT,'sun')
  
plt.plot(time, Tlist)
#plt.plot(time, Qlist)
plt.ylabel('Temp (K)')
plt.xlabel('Time (min)')
plt.show()