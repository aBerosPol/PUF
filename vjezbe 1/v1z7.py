#Gibanje Zadatak 2
#kinematika.py

import matplotlib.pyplot as pyplot
import numpy as numpy

def jednoliko_gibanje(F, m, tmax=10, dt=0.1):

    a = F / m

    t = numpy.arange(0, tmax + dt, dt)

    x = numpy.zeros (len(t))
    v = numpy.zeros (len(t))
    acc = numpy.zeros (len(t))

    acc[:] = a

    for i in range(1, len(t)):
        v [i] = v [i-1] + acc [i] * dt
        x [i] = x [i-1] + v [i] * dt

    pyplot.figure()
    pyplot.plot(t, x)
    pyplot.xlabel("t (s)")
    pyplot.ylabel("x (m)")
    pyplot.title("x - t graf")
    pyplot.grid()

    pyplot.figure()
    pyplot.plot(t, v)
    pyplot.xlabel("t (s)")
    pyplot.ylabel("v (m/s)")
    pyplot.title("v - t graf")
    pyplot.grid()

    pyplot.figure()
    pyplot.plot(t, acc)
    pyplot.xlabel("t (s)")
    pyplot.ylabel("a (m/s²)")
    pyplot.title("a - t graf")
    pyplot.grid()

    pyplot.show()