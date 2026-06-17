import numpy as numpy

def funkcija(f, x0, v0, t0, tf, dt, m):
    nKoraka = int((tf - t0) / dt) + 1 

    t = numpy.zeros(nKoraka)
    x = numpy.zeros(nKoraka)
    v = numpy.zeros(nKoraka)
    a = numpy.zeros (nKoraka)

    t[0] = t0
    x[0] = x0
    v[0] = v0
    a [0] = f(v0, x0, t0) / m

    for i in range(1, nKoraka):
        t[i] = t[i - 1] + dt
        F = f(v[i-1], x[i-1], t[i-1])
        a [i - 1] = F / m
        v[i] = v[i - 1] + a[i - 1] * dt
        x[i] = x[i-1] + v[i] * dt
    a [-1] = f(v[-1], x[-1], t[-1]) / m

    return t, x, v, a