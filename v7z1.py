import matplotlib.pyplot as pyplot
import numpy as numpy
numpy.random.seed(42)
mase_ciste = numpy.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]


def histogram(podaci, k):
    x_min = min(podaci)
    x_max = max(podaci)
    
    #a sirina razreda formula 2
    h = (x_max - x_min) / k

    #rubovi
    rubovi = []
    for i in range (k + 1):
        rubovi.append (x_min + i * h) #h je sirina razreda histograma

    #b broj pdataka u svakom razredu AI
    frekvencije = [0] * k
    for podatak in podaci:
        for i in range (k):
            if i == k - 1:
                if rubovi [i] <= podatak <= rubovi [i + 1]: #podatak je u biti x
                    frekvencije [i] += 1
                    break
            else:
                if rubovi [i] <= podatak < rubovi [i + 1]:
                    frekvencije [i] += 1
                    break

    #c ispis histograma
    for i in range(k):
        print (f"Razred {i+1}: {frekvencije [i]} podataka")

    return rubovi, frekvencije



k_razreda = 10
print("Tekstualni prikaz histograma: ")
rubovi, frekvencije = histogram(mase_ciste, k_razreda)

# Izračun sredina razreda (bina) za potrebe funkcije pyplot.bar() AI
sredine_razreda = [(rubovi[i] + rubovi[i + 1]) / 2 for i in range(k_razreda)]
sirina_stupca = rubovi[1] - rubovi[0]

pyplot.bar(sredine_razreda, frekvencije, width = sirina_stupca, edgecolor = "black") #zadnje 2 AI
pyplot.xlabel("Masa ciste zvijezde")
pyplot.ylabel("Frekvencija (broj podataka)")
pyplot.title("Histogram masa ciste zvijezde Sirius A")
pyplot.xticks(rubovi, rotation=45) #AI
pyplot.show()