import matplotlib.pyplot as pyplot
import numpy as numpy

x1 = float(input("Unesi x1 koordinatu. "))
while type (x1) != float:
    x1 = float(input("Ponovo nesi x2 koordinatu. "))

y1 = float(input("Unesi y2 koordinatu. "))
while type (y1) != float:
    y2 = float(input("Ponovo nesi y2 koordinatu. "))

x2 = float(input("Unesi x2 koordinatu. "))
while type (x2) != float:
    x2 = float(input("Ponovo nesi x2 koordinatu. "))

y2 = float(input("Unesi y2 koordinatu. "))
while type (y2) != float:
    y2 = float(input("Ponovo nesi y2 koordinatu. "))

k = (y2 - y1) / (x2 - x1)
l = y1 - (k * x1)

x = numpy.linspace (x1 - 1, x2 + 1, 1000)
y = k*x + l

pyplot.plot(x, y)
pyplot.xlabel("x os")
pyplot.ylabel("y os")
pyplot.grid(True)
pyplot.title("Jednadzba pravca")
pyplot.show()