import matplotlib.pyplot as pyplot
import numpy as numpy

def pravac (x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    l = y1 - (k * x1)
    opcija = int(input("Unesi 1 ako zelis ispis grafa na ekranu ili 2 ako zelis spremiti graf kao pdf"))
    print (f"Jednadzba tvog pravca je y = {k} * x + {l}")
    x = numpy.linspace (x1-1, x2+1, 1000)
    y = k*x + l
    pyplot.plot (x, y)
    pyplot.xlabel ("x os")
    pyplot.ylabel ("y os")
    pyplot.title("Jednadzba tvog pravca")
    pyplot.grid(True)
    if opcija == 1:
        pyplot.show()
    else:
        pyplot.savefig("grafv1z5.pdf")
        print ("Graf je spremljen kao grafv1z5.pdf")

x1 = float(input("Unesi x1 koordinatu. "))
y1 = float(input("Unesi y2 koordinatu. "))
x2 = float(input("Unesi x2 koordinatu. "))
y2 = float(input("Unesi y2 koordinatu. "))

pravac (x1, y1, x2, y2)