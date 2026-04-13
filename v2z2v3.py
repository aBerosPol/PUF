import numpy as numpy
import matplotlib.pyplot as pyplot
#AI koristen za formule (matematika)

v0 = 10
theta = numpy.radians (60)
g = 9.81

#analiticko rjesenje za domet
R_exact = (v0**2 * numpy.sin(2 * theta)) / g

dt_values = numpy.linspace (0.01, 0.1, 1000) #raspon koraka
errors = []

for dt in dt_values:
    x, y = 0, 0
    vx = v0 * numpy.cos (theta)
    vy = v0 * numpy.sin (theta)
    
    #eulerova metoda
    while y >= 0:
        x += vx * dt
        y += vy * dt
        vy -= g * dt
    
    R_num = x
    
    #relativna greska
    error = abs (R_num - R_exact) / R_exact
    errors.append (error)

pyplot.figure ()
pyplot.plot (dt_values, errors) #crta graf s obe logaritamske osi
pyplot.xlabel ("Δt (s)")
pyplot.ylabel ("Relativna pogreska")
pyplot.title ("Ovisnost relativne pogreske o vremenskom koraku")
pyplot.grid (True)
pyplot.show ()