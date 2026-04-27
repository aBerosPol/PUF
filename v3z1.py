import numpy as numpy
import matplotlib.pyplot as pyplot


class Projectile:
    def __init__(self, x0, y0, v0, angle_deg, masa=1, koef=0.05, g=9.81):
        self.x0 = x0 #x0 pocetni polozaj na x
        self.y0 = y0 #y0 pocetni polozaj na y
        self.v0 = v0 #v0 pocetna brzina
        self.angle = numpy.radians(angle_deg) #kut izbacaja
        self.m = masa #masa tijela
        self.k = koef #koeficijent otpora zraka
        self.g = g #akceleracija

        self.vx0 = v0 * numpy.cos(self.angle)
        self.vy0 = v0 * numpy.sin(self.angle)

    def akceleracija(self, vx, vy):
        #po forumuli Fo = -koef * v
        #akceleracije negativan broj jer usporava
        ax = -(self.k / self.m) * vx #akceleracija po x, po formuli ma = -k*v (sve po x)
        ay = -self.g - (self.k / self.m) * vy #akceleracija po y, po formuli ma = -mg - k*v (sve po y)
        return ax, ay

    def euler(self, dt):
        x = self.x0
        y = self.y0
        vx = self.vx0
        vy = self.vy0
        t = 0

        #liste u koje ce se spremat svi polozaji za graf poslije, na pocetku su sve vrijednosti 0
        X = [x]
        Y = [y]
        T = [t]

        while y >= 0: #dok ne padne na tlo
            ax, ay = self.akceleracija(vx, vy)

            #euler korak, AI napisao 4 formule
            x = x + vx * dt
            y = y + vy * dt
            vx = vx + ax * dt
            vy = vy + ay * dt

            t += dt

            #dodaje sve u liste
            X.append(x)
            Y.append(y)
            #T.append(t)

        return numpy.array(X), numpy.array(Y), x #, numpy.array(T)



projektil = Projectile(
    x0=0,
    y0=0,
    v0=40,
    angle_deg=45, 
    masa=1,
    koef=0.08
)

dt_values = [0.5, 0.2, 0.1, 0.05, 0.01]


prethodni_domet = 0

for dt in dt_values:
    x, y, domet = projektil.euler(dt)
    pyplot.plot(x, y, label=f"dt = {dt}, (Domet{domet:.1f}m)") #domet:.1f kaze da ce bit float i da sadrzi samo jedno mjesto nakon decimalnog zareza

    if prethodni_domet != 0:
        razlika = abs (domet - prethodni_domet)
        print(f"dt: {dt} | Trenutni domet: {domet:.2f} | Razlika: {razlika:.2f}")

        if razlika < 1.5:
            print(f"Korak s dt = {dt} je dovoljno precizan.")

    prethodni_domet = domet

#kod gleda koliko se polozaj tijela promijenio u odnosu na prethodni po razlicitim vremenskim intervalima

pyplot.title("Kosi hitac s otporom zraka - Eulerova metoda")
pyplot.xlabel("x [m]")
pyplot.ylabel("y [m]")
pyplot.grid(True)
pyplot.legend()

#iduce 2 linije AI
pyplot.xlim(left=0)
pyplot.ylim(bottom=0)

pyplot.show()