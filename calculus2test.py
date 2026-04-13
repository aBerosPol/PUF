import numpy as np
import matplotlib.pyplot as plt
import calculus2

def f(x):
    return np.sin(x) + 0.5*x

def f_integral(x):
    return -np.cos(x) + 0.25*x**2

a, b = 0, 10

n_values = [5, 20, 100]

x_dense = np.linspace(a, b, 1000)
y_analytical = f_integral(x_dense)

plt.figure(figsize=(10,6))

plt.plot(x_dense, y_analytical, label="Analitički integral", linewidth=2)

for n in n_values:
    #trapezna metoda
    I_trap = [calculus.trapezoidal_integral(f, a, xi, n) for xi in x_dense]
    plt.plot(x_dense, I_trap, '--', label=f"Trapez n={n}")

    #pravokutnici (koristim gornju aproksimaciju za graf)
    I_rect_upper = [calculus.rectangle_integral(f, a, xi, n)[1] for xi in x_dense]
    plt.plot(x_dense, I_rect_upper, ':', label=f"Pravokutnik (gornja) n={n}")

plt.title("Numerička integracija")
plt.xlabel("x")
plt.ylabel("Integral")
plt.legend()
plt.grid()
plt.show()