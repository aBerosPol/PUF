import numpy as numpy
sumA = 0
n = 10

#aritmeticka sredina
for i in range (n+1):
    sumA += i

arithm = sumA / n

print (f"Aritmeticka sredina brojeva do {n} je {arithm}")


#standardna devijacija triba bit cca 2.87
sumB = 0
brojnik = 0
nazivnik = n * (n-1)

for i in range (1, n + 1):
    brojnik += ((i - arithm)**2)

stDev = numpy.sqrt(brojnik / nazivnik)
print (f"Standardna devijacija brojeva do 10 je {stDev:.5f}") #zaokruzeno na 5 decimala da lijepo izgleda