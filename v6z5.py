import numpy as np
# 5 mjerenja temperature vrenja vode [ u stupnjevima Celzijusa ]
malo_n = [99.8 , 100.1 , 99.9 , 100.2 , 100.0]

# 10000 mjerenja istog eksperimenta ( simulacija )
np . random . seed (42)
veliko_n = np . random . normal ( loc =100.0 , scale =0.2 , size =10000) . tolist ()



def analiza(podaci, naziv):
    n = len(podaci)
    avg = np.mean(podaci)

    sigmaN = np.std(podaci, ddof=0)

    #AI
    # uzoračka standardna devijacija (dijeljenje s n-1)
    s = np.std(podaci, ddof=1)

    # relativna razlika
    rel_razlika = abs(s - sigmaN) / s * 100
    #/AI

    print(f"\n--- {naziv} ---")
    print(f"Broj mjerenja n = {n}")
    print(f"Srednja vrijednost x̄ = {avg:.6f}")
    print(f"σ_n (ddof=0) = {sigmaN:.6f}")
    print(f"s   (ddof=1) = {s:.6f}")
    print(f"Relativna razlika = {rel_razlika:.6f}%")

#AI
analiza(malo_n, "MALI SKUP")
analiza(veliko_n, "VELIKI SKUP")

#AI odgovori
print("\nZaključak:")
print("Kako n raste, razlika izmedu s i sigma se smanjuje.")
print("Za veliki broj mjerenja s je proporcionalan sigma_n.")
print("np.std() po defaultu koristi ddof=0, tj. dijeljenje s n. To je ispravno kada imamo cijelu populaciju")
print("Za uzorak iz populacije obično koristimo ddof=1.") 