import numpy as np
import matplotlib.pyplot as plt
import v2calculus2v3
#AI koristen za formule (matematika)

def f(x):
    return np.sin(x) + 0.5*x

def f_integral(x):
    return -np.cos(x) + 0.25*x**2

a, b = 0, 10

n_values = np.arange(1, 500, 2)

x_dense = np.linspace(a, b, 100000)

plt.figure(figsize=(10,6))
y_analytical = f_integral(b) - f_integral(a)

I_trap_vrijednosti = []
I_rect_vrijednosti = []


for n in n_values:
    I_trap_vrijednosti.append(v2calculus2v3.trapezoidal_integral(f, a, b, n))
    I_rect_vrijednosti.append(v2calculus2v3.rectangle_integral(f, a, b, n))

plt.scatter(n_values, I_trap_vrijednosti, label="Trapezna metoda")

plt.plot(n_values, I_rect_vrijednosti, label=f"Pravokutna metoda")

plt.axhline(y = y_analytical, label=f"Analiticki integral")

plt.title("Numerička integracija")
plt.xlabel("n")
plt.ylabel("Integral")
plt.legend()
plt.grid()
plt.show()