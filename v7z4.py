import matplotlib.pyplot as pyplot
import numpy as numpy

numpy.random.seed(42)
mase_ciste = numpy.random.normal(loc=2.06, scale=0.05, size=57).tolist()
pogreske = [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02] #izvuceno iz zadanog koda
mase = mase_ciste + pogreske

#funkcija iz v7z3.py
def izracunaj_medijan(podaci):
    sortirani = sorted(podaci)
    n = len(sortirani)
    if n % 2 != 0:
        return sortirani[((n + 1) // 2) - 1]
    else:
        return (sortirani[(n // 2) - 1] + sortirani[n // 2]) / 2

#skup sa svim mjerenjima (ukljucuje pogreske)
sredina_sve = sum(mase) / len(mase)
medijan_sve = izracunaj_medijan(mase)
razlika_sve = abs(sredina_sve - medijan_sve)

#skup nakon uklanjanja pogreska
sredina_cisto = sum(mase_ciste) / len(mase_ciste)
medijan_cisto = izracunaj_medijan(mase_ciste)
razlika_cisto = abs(sredina_cisto - medijan_cisto)



promjena_sredine = abs(sredina_sve - sredina_cisto)
promjena_medijana = abs(medijan_sve - medijan_cisto)

print("Rezultati za sve mase prije uklanjanja pogresaka:")
print(f"Aritmetička sredina: {sredina_sve:.4f}")
print(f"Medijan: {medijan_sve:.4f}")
print(f"Razlika izmedu njih: {razlika_sve:.4f}\n")

print("Rezultati nakon uklanjanja pogresaka:")
print(f"Aritmetička sredina: {sredina_cisto:.4f}")
print(f"Medijan: {medijan_cisto:.4f}")
print(f"Razlika izmedu njih: {razlika_cisto:.4f}\n")

print("Utjecaj pogresaka na statistiku:")
print(f"Srednja vrijednost se promijenila za: {promjena_sredine:.4f}")
print(f"Medijan se promijenio za: {promjena_medijana:.4f}\n")

#AI - vizualizacija histograma
frekvencije, rubovi, _ = pyplot.hist(mase, bins=30, edgecolor="black", color="gainsboro", alpha=0.7, label="Sva mjerenja (s pogreškama)")

# AI - Ucrtavanje vertikalnih linija
pyplot.axvline(sredina_sve, color="red", linestyle="dashed", linewidth=2.5, label=f"Sredina s pogreškama ({sredina_sve:.2f})")
pyplot.axvline(medijan_sve, color="orange", linestyle="dashdot", linewidth=2.5, label=f"Medijan s pogreškama ({medijan_sve:.2f})")
pyplot.axvline(sredina_cisto, color="blue", linestyle="dotted", linewidth=2.5, label=f"Sredina bez pogrešaka ({sredina_cisto:.2f})")
pyplot.axvline(medijan_cisto, color="green", linestyle="solid", linewidth=2, label=f"Medijan bez pogrešaka ({medijan_cisto:.2f})")



pyplot.xlabel("Masa zvijezde")
pyplot.ylabel("Frekvencija")
pyplot.title("Usporedba reaktivnosti aritmeticke sredine i medijana na pogreske")
pyplot.legend()
pyplot.grid (True)
pyplot.show()