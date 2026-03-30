import numpy as numpy
from particle import Particle

v0 = 10
theta = numpy.pi/4
x0 = 0
y0 = 0

particle = particlee (v0, theta, x0, y0)

rangeNumeric = particlee.range (dt = 0.001)

g = 9.81
rangeAnalytic = (v0**2 * numpy.sin(2*theta)) / g

print (f"Numericki domet je {rangeNumeric} \n Analiticki domet je {rangeAnalytic} \n Odstupanje iznosi {abs(rangeNumeric - rangeAnalytic)}")