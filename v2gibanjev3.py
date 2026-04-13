import numpy as numpy
from v2particlev3 import Particle
#AI koristen za formule (matematika)

v0 = 10
theta = numpy.pi/4
x0 = 0
y0 = 0

particle = Particle (v0, theta, x0, y0)

rangeNumeric = particle.range (dt = 0.001)

g = 9.81
rangeAnalytic = (v0**2 * numpy.sin(2*theta)) / g

if rangeNumeric == rangeAnalytic:
    print ("Analiticko rjesenje se poklapa s numerickim.")
else:
    print ("Analiticko rjesenje se ne poklapa s numerickim.")

print (f"Numericki domet je {rangeNumeric} \n Analiticki domet je {rangeAnalytic} \n Odstupanje iznosi {abs(rangeNumeric - rangeAnalytic)}")