# M = dt * phi
import matplotlib.pyplot as pyplot
import numpy as np

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] #[Nm]
phi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] #[rad]

phi_n=np.array(phi)

#srednja vrijednost svakog M * phi
sumA = 0

for value in M:
    sumA += value

arithm = sumA / len(M)

print (f"Aritmeticka sredina brojeva u listi M je {arithm:.5f}") #na 5 decimala

#srednja vrijednost umnoska
sumMPhi = 0 #suma umnozaka M * phi
for valueM in M:
    for valuePhi in phi:
        sumMPhi += valueM * valuePhi
avgMPhi = sumMPhi / len(M)

print (f"Aritmeticka sredina umnoska M * phi iznosi {sumMPhi:.5f}")


#srednja vrijednost kvadrata nezavisne varijable (kut phi)
sumPhySqrd = 0

for valuePhi in phi:
    sumPhySqrd += (valuePhi**2)

avgPhiSqrd = sumPhySqrd / len(phi)

print (f"Prosjecna vrijednost kvadrata kuteva iznosi {avgPhiSqrd:.5f}")

#srednja vrijednost kvadrata zavisne varijable 
sumMsqrd = 0

for valueM in M:
    sumMsqrd += (valueM**2)

avgMsqrd = sumMsqrd / len(M)

#formula 4 - nagib pravca
a = avgMPhi / ( avgPhiSqrd)

#formula 5 - standardna devijacija
sigma = ((1/len(M)) * ((avgPhiSqrd / avgMsqrd) - a**2))**0.5

xOs = [0, max(phi)]
yOs = [0, max(M)]

#pyplot.plot (phi, M)
pyplot.plot(phi, phi_n*a)
#ne znam sto tocno trebam scatterat     pyplot.scatter (phi, M)
pyplot.title ("Odredivanje modula torzije Dt")
pyplot.xlabel ("Kut izbacaja [rad]")
pyplot.ylabel ("Iznos momenta sile [Nm]")
pyplot.grid (True)
pyplot.show ()