import numpy as numpy
import matplotlib.pyplot as pyplot

h0 = 0.54 # m
m = 0.5257 # kg
e = 4.025e-3 # m
r = e #posli sam zezla formulu

h = [0.14, 0.17, 0.19, 0.22, 0.25, 0.28, 0.31, 0.34, 0.37, 0.40] # m
t_mean = [1.740, 1.793, 2.043, 2.190, 2.280, 2.417, 2.540, 2.640, 2.670, 2.813] # s

np_h = numpy.array(h)
np_t = numpy.array(t_mean)

g = 9.81

s = np_h #prijedeni put
log_s = numpy.log(s)
log_t = numpy.log(t_mean)

n = len (log_t)
sum_x = numpy.sum (log_t)
sum_y = numpy.sum (log_s)
sum_xy = numpy.sum(log_t * log_s)
sum_x2 = numpy.sum(log_t ** 2)

#nagib A i odsjecak B
A = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
B = (sum_y - A * sum_x) / n

#pogreske
s_y = numpy.sqrt(numpy.sum((log_s - (A * log_t + B)) ** 2) / (n - 2))
err_A = s_y / numpy.sqrt(n * sum_x2 - sum_x ** 2)
err_B = s_y * numpy.sqrt (1/n + sum_x**2 / (n * sum_x2 - sum_x**2))

#rjesenje od a
print (f"Nagib A = {A:.4f} +- {err_A:.4f}")
print (f"Odsjecak B = {B:.4f} +- {err_B:.4f}")

a_ef_log = 2 * numpy.exp (B)
err_a_ef_log = 2 * numpy.exp (B) * err_B

print (f"a_ef iz log prikaza = {a_ef_log:.4f} m/s^(2) +- {err_a_ef_log:.4f} m/s^(2)")


#graf
t_fit = numpy.linspace (min(log_t), max(log_t), 100)
log_s_fit = A * t_fit + B

#pyplot.errorbar (log_t, log_s, label = "Mjerenja") #AI
pyplot.scatter (log_t, log_s)
pyplot.plot (t_fit, log_s_fit, label = "Linearna regresija", color = "red") #AI
pyplot.xlabel ("log(t) [s]")
pyplot.ylabel ("log(s) [m]")
pyplot.title ("Logaritamski graf log(s) - log(t)")
pyplot.grid (True)
pyplot.legend

#dio b
#formula 3
X_b = np_t ** 2
Y_b = s
#Y_b = snagib_b = numpy.sum (X_b * Y_b) / numpy.sum (X_b ** 2)
nagib_b = numpy.sum (X_b * Y_b) / numpy.sum (X_b ** 2)

s_y_b = numpy.sqrt (numpy.sum ((Y_b - nagib_b * X_b) ** 2) / (n - 1))
err_nagib_b = s_y_b / numpy.sqrt (numpy.sum (X_b ** 2))

a_ef_kvadrat = 2 * nagib_b
err_a_ef_kvadrat = 2 * err_nagib_b

print (f"Nagib pravca s - t^(2) = {nagib_b:.4f} +- {err_nagib_b:.4f}")
print (f"a_ef = {a_ef_kvadrat:.4f} +- {err_a_ef_kvadrat:.4f} m/s^(2)")

#graf
pyplot.subplot (1, 2, 2)
pyplot.scatter (X_b, Y_b, label = "Mjerenja")
x_fit_b = numpy.linspace (0, max(X_b), 100) #krece od 0 jer prolazi kroz ishodiste
pyplot.plot (x_fit_b, nagib_b * x_fit_b, label = "Fit kroz ishodiste")
pyplot.xlabel ("t^2 [s^2]")
pyplot.ylabel ("s [m]")
pyplot.title ("s - t^2 graf")
pyplot.grid (True)
pyplot.legend()
pyplot.tight_layout() #AI
pyplot.show()

#c
Iz = m * (r ** 2) * (g/ a_ef_kvadrat - 1)
der_a_ef = - m * (r ** 2) * (g / a_ef_kvadrat ** 2)
err_Iz = abs (der_a_ef) * err_a_ef_kvadrat

print (f"Moment tromosti Iz = {Iz:.4e} kg m^(2)")
print (f"Izvedena pogreska err_Iz = {err_Iz:.4e} kg m^(2)")
pyplot.show()