import matplotlib.pyplot as pyplot
import numpy as numpy

numpy.random.seed(42)
mase_ciste = numpy.random.normal(loc=2.06, scale=0.05, size=57).tolist()

#aritm sredina
aritmeticka_sredina = sum(mase_ciste) / len(mase_ciste)

#medijan
sortirane_mase = sorted(mase_ciste) #AI - sortira ih po velicini
n = len(sortirane_mase)  #jer je n = 57 neparan broj

indeks_medijana = ((n + 1) // 2) - 1
medijan = sortirane_mase[indeks_medijana]

print(f"Izračunata aritmetička sredina: {aritmeticka_sredina:.4f}")
print(f"Izračunani medijan (29. podatak u nizu): {medijan:.4f}")



k_razreda = 10


#AI
frekvencije_gotove, rubovi_gotovi, _ = pyplot.hist(
    mase_ciste, bins=k_razreda, edgecolor="black", color="lightblue", alpha=0.7, label="Ugrađeni histogram"
)

#\AI

#AI ucrtava vertikalne linije
pyplot.axvline(aritmeticka_sredina, color="red", linestyle="dashed", linewidth=2, label=f"Aritmetička sredina ({aritmeticka_sredina:.3f})")
pyplot.axvline(medijan, color="green", linestyle="dotted", linewidth=2, label=f"Medijan ({medijan:.3f})")


pyplot.xlabel ("Masa ciste zvijezde")
pyplot.ylabel ("Frekvencija (broj podataka)")
pyplot.title ("Ugradeni histogram s oznacenom sredinom i medijanom")
pyplot.xticks (rubovi_gotovi, rotation=45)
pyplot.legend ()
#
pyplot.grid (axis='y', alpha=0.3)
pyplot.show()

#AI
print("Ugrađene frekvencije iz Zadaka 2: ", [int(f) for f in frekvencije_gotove])
