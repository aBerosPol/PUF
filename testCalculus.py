import numpy as np
import matplotlib.pyplot as plt
import calculus

#kubna funkcija
def cubic (x):
    return x**3 + 2*x**2 - x + 1

def cubic_derivative(x):
    return 3*x**2 + 4*x - 1


#trigonomoterijska funkcija
def trig (x):
    return np.sin(x)

def trig_derivative (x):
    return np.cos(x)

x_min, x_max = -5, 5 #interval

#analiticko rjeseje
x_dense = np.linspace(x_min, x_max, 1000)

#test
eps_values = [1e-1, 1e-3, 1e-5]

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)

#analiticka derivacija
plt.plot(x_dense, cubic_derivative(x_dense), label="Analitička", linewidth=2)

for eps in eps_values:
    x_vals, d_vals = calculus.derivative_range(
        cubic, x_min, x_max, eps=eps, step=0.2, method="three-step"
    )
    plt.plot(x_vals, d_vals, linestyle="--", label=f"eps={eps}")

plt.title("Kubna funkcija")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)

plt.plot(x_dense, trig_derivative(x_dense), label="Analitička", linewidth=2)

for eps in eps_values:
    x_vals, d_vals = calculus.derivative_range(
        trig, x_min, x_max, eps=eps, step=0.2, method="three-step"
    )
    plt.plot(x_vals, d_vals, linestyle="--", label=f"eps={eps}")

plt.title("Trigonometrijska funkcija")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()