from v3z1 import Projectile
import numpy as numpy
import matplotlib.pyplot as pyplot


#nadogradujem klasu
class ProjectileRK4(Projectile):
    def rk4(self, dt):
        x = self.x0
        y = self.y0
        vx = self.vx0
        vy = self.vy0
        t = 0

        X = [x]
        Y = [y]

        while y >= 0:

            #derivacija sustava: dx/dt = vx, dy/dt = vy, dvx/dt = ax, dvy/dt = ay, AI formule
            def f(x, y, vx, vy):
                ax, ay = self.akceleracija(vx, vy)
                return numpy.array([vx, vy, ax, ay])

            stanje = numpy.array([x, y, vx, vy])

            k1 = f(x, y, vx, vy) #nagib na pocetku intervala
            k2 = f(*(stanje + 0.5 * dt * k1)) #nagib oko sredine intervala
            k3 = f(*(stanje + 0.5 * dt * k2)) #nagib na sredini intervala
            k4 = f(*(stanje + dt * k3)) #nagib na kraju intervala

            stanje = stanje + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)

            x, y, vx, vy = stanje
            #kraj AI formula
            t += dt

            X.append(x)
            Y.append(y)

        return numpy.array(X), numpy.array(Y), x


# stvaranje objekta
projektil = ProjectileRK4(
    x0=0,
    y0=0,
    v0=40,
    angle_deg=45,
    masa=1,
    koef=0.08
)

dt = 0.01

#euler
xe, ye, domet_e = projektil.euler(dt)

#RK4
xr, yr, domet_rk = projektil.rk4(dt)



pyplot.plot(xe, ye, label=f"Euler, dt={dt}, domet={domet_e:.2f} m")
pyplot.plot(xr, yr, label=f"RK4, dt={dt}, domet={domet_rk:.2f} m")

pyplot.title(f"Usporedba Eulerove i Runge-Kutta metode 4. reda, dt = {dt}")
pyplot.xlabel("x [m]")
pyplot.ylabel("y [m]")
pyplot.grid(True)
pyplot.legend()

#iduce 2 linije AI
pyplot.xlim(left=0)
pyplot.ylim(bottom=0)

pyplot.show()


print(f"Euler domet: {domet_e:.4f} m")
print(f"RK4 domet: {domet_rk:.4f} m")
print(f"Razlika: {abs(domet_e-domet_rk):.4f} m")