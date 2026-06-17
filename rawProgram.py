import matplotlib.pyplot as pyplot
import numpy as numpy
from rawModul import funkcija


print ("TESTIRANJE MODULA")
x0input = float (input("Unesi pocetni polozaj (x0): "))
v0input = float (input("Unesi pocetnu brzinu (v0):"))
tinput = float(input("Unesi duljinu vremenskog intervala (tf): "))

dt = 0.01
m = 1

F0 = 5
def Fconst (v, x, t):
    return F0

t_a, x_a, v_a, a_a = funkcija(Fconst, x0input, v0input, 0, tinput, dt, m)

k = 10.0

def harmonijskiOscilator (v, x, t):
    return -k * x

t_b, x_b, v_b, a_b = funkcija (harmonijskiOscilator, x0input, v0input, 0, tinput, dt, m)

def proizvolja_sila (v, x, t):
    #2t - v + x
    return 2*t - v + x

t_c, x_c, v_c, a_c = funkcija (proizvolja_sila, x0input, v0input, 0, tinput, dt, m)

pyplot.subplot (3, 3, 1)
pyplot.plot (t_a, x_a)
pyplot.title ("F = const.: x [m]")
pyplot.xlabel ("Vrijeme [s]")
pyplot.ylabel ("Polozaj [m]")
pyplot.grid (True)

pyplot.subplot (3, 3, 2)
pyplot.plot (t_a, v_a)
pyplot.title ("F = const.: v [m/s]")
pyplot.xlabel ("Vrijeme [s]")
pyplot.ylabel ("Brzina [m/s]")
pyplot.grid (True)

pyplot.subplot (3, 3, 3)
pyplot.plot (t_a, a_a)
pyplot.title ("F = const.: a [m/(s^2)]")
pyplot.xlabel ("Vrijeme [s]")
pyplot.ylabel ("Akceleracija [m/s^2]")
pyplot.grid (True)

pyplot.subplot (3, 3, 4)
pyplot.plot (t_b, x_b)
pyplot.title ("F = -kx: x [m]")
pyplot.xlabel ("Vrijeme [s]")
pyplot.ylabel ("Polozaj [m]")
pyplot.grid (True)

pyplot.subplot (3, 3, 5)
pyplot.plot (t_b, v_b)
pyplot.title ("F = -kx: v [m/s]")
pyplot.xlabel ("Vrijeme [s]")
pyplot.ylabel ("Brzina [m/s]")
pyplot.grid (True)

pyplot.subplot (3, 3, 6)
pyplot.plot (t_b, a_b)
pyplot.title ("F = -kx: a [m/s^2]")
pyplot.xlabel ("Vrijeme [s]")
pyplot.ylabel ("Akceleracija [m/s^2]")
pyplot.grid (True)

pyplot.subplot (3, 3, 7)
pyplot.plot (t_c, x_c)
pyplot.title ("F = 2t - v + x: x [m]")
pyplot.xlabel ("Vrijeme [s]")
pyplot.ylabel ("Polozaj [m]")
pyplot.grid (True)

pyplot.subplot (3, 3, 8)
pyplot.plot (t_c, v_c)
pyplot.title ("F = 2t - v + x: v [m/s]")
pyplot.xlabel ("Vrijeme [s]")
pyplot.ylabel ("Brzina [m/s]")
pyplot.grid (True)

pyplot.subplot (3, 3, 9)
pyplot.plot (t_c, a_c)
pyplot.title ("F = 2t - v + x: a [m/s^2]")
pyplot.xlabel ("Vrijeme [s]")
pyplot.ylabel ("Akceleracija [m/s^2]")
pyplot.grid (True)

pyplot.tight_layout()
pyplot.show()