import numpy as numpy
import matplotlib.pyplot as pyplot
#AI koristen za formule (matematika)

class Particle:
    def __init__(self, v0 = 0, theta = 0, x0 = 0, y0 = 0):
        self.v0 = v0
        self.theta = theta
        self.x0 = x0
        self.y0 = y0

        self.g = 9.81

        #pocetna brzina na komponente
        self.vx0 = v0 * numpy.cos(theta)
        self.vy0 = v0 * numpy.sin(theta)

        #trenutne vrijednosti
        self.reset()

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.vx0
        self.vy = self.vy0
        self.t = 0 #resetira vrijeme na 0

        self.x_lista = [self.x]
        self.y_lista = [self.y]

    def __move (self, dt):
        #Eulerove jednadybe
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy -= self.g * dt
        self.t += dt
        self.x_lista.append(self.x)

        self.y_lista.append(self.y)

    def range (self, dt=0.02):
        self.reset()

        while self.y >= 0:
            self.__move (dt)

        return self.x
    
    def plot_trajectory (self, dt = 0.01):
        self.reset()

        while self.y >= 0:
            self.__move (dt)
        
        pyplot.plot (self.x_lista, self.y_lista)
        pyplot.xlabel ("x [m]")
        pyplot.ylabel ("y [m]")
        pyplot.title ("putanja projektila")
        pyplot.grid (True)
        pyplot.show ()