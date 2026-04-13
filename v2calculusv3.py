import numpy as numpy
#AI koristen za formule (matematika)

def derivative_at_point (f, x, eps=0.1, method="three-step"):
    if method == "two-step":
        #diferencija AI
        return (f(x + eps) - f(x)) / eps

    elif method == "three-step":
        #diferencija
        return (f(x + eps) - f(x - eps)) / (2 * eps)

    else:
        raise ValueError ("Nepoznata metoda. Koristite 'two-step' ili 'three-step'.")


def derivative_range (f, x_min, x_max, eps=0.1, step=0.1, method="three-step"):
    x_values = numpy.arange (x_min, x_max, step)
    derivatives = []

    for x in x_values:
        d = derivative_at_point (f, x, eps, method)
        derivatives.append(d)

    return x_values, numpy.array (derivatives)