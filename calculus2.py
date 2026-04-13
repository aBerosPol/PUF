import numpy as np

def rectangle_integral(f, a, b, n):
    x = np.linspace(a, b, n+1)
    dx = (b - a) / n

    #donja i gornja aproksimacija
    lower_sum = np.sum([min(f(x[i]), f(x[i+1])) * dx for i in range(n)])
    upper_sum = np.sum([max(f(x[i]), f(x[i+1])) * dx for i in range(n)])

    return lower_sum, upper_sum


def trapezoidal_integral(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    dx = (b - a) / n

    return (dx/2) * np.sum(y[:-1] + y[1:])