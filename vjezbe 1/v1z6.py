#Gibanje Zadatak 1

import numpy as numpy
import matplotlib.pyplot as pyplot

F = int(input("Unesi iznos sile na cesticu mase m u Newtonima. "))
m = int(input("Unesi masu cestice m u kilogramima. "))

a = F / m

dt = 0.1
t = numpy.arange (0, 10 +dt, dt) #numpy.arange stvara listu u tom rasponu kojeg mu dam

x = numpy.zeros(len(t)) #numpy.zeros stvara niz nula duljine len(t)
v = numpy.zeros(len(t))
acc = numpy.zeros(len(t))

acc [:] = a

for i in range (1, len(t)):
    v[i] = v[i - 1] + acc [i] * dt
    x [i] = x [i - 1] + v [i] * dt

pyplot.figure ()
pyplot.plot (t, x)
pyplot.xlabel ("t (s)")
pyplot.ylabel ("x (m)")
pyplot.grid(True)

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