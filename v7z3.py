import numpy as numpy

numpy.random.seed(42)
mase_ciste = numpy.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]

#formula 2
def medijan(podaci):
    sortirani = sorted(podaci) #sortira po velicini
    n = len(sortirani)

    if n % 2 != 0:
        indeks = ((n + 1) // 2) - 1 #formula za neparan n
        return sortirani[indeks]
    else: #formula za paran n
        indeks1 = (n // 2) - 1
        indeks2 = (n // 2)
        
        vrijednost1 = sortirani[indeks1]
        vrijednost2 = sortirani[indeks2]
        
        return (vrijednost1 + vrijednost2) / 2



a = [3, 1, 4, 1, 5, 9, 2, 6]
b = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print(f"Medijan skupa a: {medijan(a)}")
print(f"Medijan skupa b: {medijan(b)}")

#primjena na mase #AI

print("\n--- Primjena na skup 'mase' ---")
moj_medijan_mase = medijan(mase)
numpy_medijan_mase = numpy.median(mase)

print(f"Vlastita funkcija (n={len(mase)}): {moj_medijan_mase:.4f}")
print(f"Provjera pomoću numpy.median(): {numpy_medijan_mase:.4f}")
#\AI
if numpy_medijan_mase == moj_medijan_mase:
    print ("Tocno")