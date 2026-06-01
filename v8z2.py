import numpy as numpy
import matplotlib.pyplot as pyplot

kut_deg = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
T_120 = [0.8020, 0.8187, 0.8327, 0.8660, 0.8980, 0.9153, 0.9293, 0.9653, 0.9747, 1.0200, 1.0373, 1.1160, 1.1780, 1.2733, 1.4180, 1.6373, 1.9100, 2.5460]
T_240 = [1.0140, 1.0320, 1.0433, 1.0673, 1.0840, 1.1320, 1.1440, 1.1720, 1.1980, 1.2293, 1.2813, 1.3573, 1.4200, 1.5600, 1.7413, 1.9840, 2.4473, 3.1573]

np_kut = numpy.array(kut_deg)
np_T120 = numpy.array(T_120)
np_T240 = numpy.array(T_240)

g = 9.81

kut_rad = numpy.radians(np_kut)

#y = T^2, x = (4 * pi^2) / (g * cos(theta))
Y_120 = np_T120 ** 2
Y_240 = np_T240 ** 2
X = (4 * (numpy.pi ** 2)) / (g * numpy.cos(kut_rad))

#nagib preko formule 3    a = sum(x*y) / sum(x^2)
l_fit_120 = numpy.sum(X * Y_120) / numpy.sum(X ** 2)
l_fit_240 = numpy.sum(X * Y_240) / numpy.sum(X ** 2)

#u metrima za pogresku
L1_stvarno = 0.120 # m
L2_stvarno = 0.240 # m

rel_err_120 = abs(l_fit_120 - L1_stvarno) / L1_stvarno
rel_err_240 = abs(l_fit_240 - L2_stvarno) / L2_stvarno



print(f"Za L = 120 mm izmjerena efektivna duljina l = {l_fit_120:.4f} m")
print(f"Relativna pogreska = {rel_err_120 * 100:.2f} %\n")

print(f"Za L = 240 mm izmjerena efektivna duljina l = {l_fit_240:.4f} m")
print(f"Relativna pogreska = {rel_err_240 * 100:.2f} %\n")



kut_fit_deg = numpy.linspace(0, 85, 200)
kut_fit_rad = numpy.radians(kut_fit_deg)


def izracunaj_T(kutovi_rad, l):
    return 2 * numpy.pi * numpy.sqrt(l / (g * numpy.cos(kutovi_rad)))

#graf
pyplot.scatter(np_kut, np_T120, label="Mjerenja (L=120 mm)")
pyplot.plot(kut_fit_deg, izracunaj_T(kut_fit_rad, l_fit_120), label="Teorijski fit (L = 120mm)")
pyplot.scatter(np_kut, np_T240, label="Mjerenja (L=240 mm)")
pyplot.plot(kut_fit_deg, izracunaj_T(kut_fit_rad, l_fit_240), label="Teorijski fit (L = 240mm)")

pyplot.xlabel("Kut theta [deg]")
pyplot.ylabel("Period T [s]")
pyplot.title("Ovisnost perioda o kutu")
pyplot.grid(True)
pyplot.legend()
pyplot.show()