def preciznost_test(N):
    broj = 5.0
    # N puta dodaj 1/3
    for _ in range(N):
        broj += 1/3
    # N puta oduzmi 1/3
    for _ in range(N):
        broj -= 1/3
    return broj

iteracije = [200, 2000, 20000]

for n in iteracije:
    konacni_rezultat = preciznost_test(n)
    print(f"Za N = {n:5}, konačni rezultat je: {konacni_rezultat}")

print ("Rjesnje je krivo jer računalo ne moze savrseno zapisati 1/3 u binarnom sustavu, pa se te sitne greske pri zaokruzivanju akumuliraju kroz N iteracija.")