import numpy as np
import matplotlib.pyplot as plt

def simulacijaGibanja (naboj, masa, polje_E, polje_B, trajanje, korak):
    #pocetni uvjeti
    polozaj = np.array([0.0, 0.0, 0.0])
    brzina = np.array([1.0, 1.0, 1.0])  #sve 3 komponente razlicite od 0
    
    putanja_x = []
    putanja_y = []
    putanja_z = []
    
    broj_koraka = int(trajanje / korak) #da bude cijeli broj
    
    for i in range(broj_koraka):
        #lorentzova sila: F = q * (E + v x B)
        sila_elektricna = naboj * polje_E #generalna formula
        sila_magnetska = naboj * np.cross(brzina, polje_B) #np.cross AI, cross product
        ukupna_sila = sila_elektricna + sila_magnetska #jer se sile zbrajaju
        
        # akceleracija a = F / m
        ubrzanje = ukupna_sila / masa
        
        # brzina i polozaj
        brzina = brzina + ubrzanje * korak #korak je dt
        polozaj = polozaj + brzina * korak
        
        # sprema x y i z komponentu da bi graf mogao biti u 3D
        putanja_x.append(polozaj[0])
        putanja_y.append(polozaj[1])
        putanja_z.append(polozaj[2])
        
    return putanja_x, putanja_y, putanja_z

#simulacija
vrijeme_trajanja = 20.0
dt = 0.01
masa_cestice = 1.0 #za lakse racunanje

#parametri za scenarije, AI ideja za scenarije
scenariji = [
    {
        "naslov": "1. Samo B polje (cista spirala)",
        "E": np.array([0.0, 0.0, 0.0]),
        "B": np.array([0.0, 0.0, 2.0])
    },
    {
        "naslov": "2. E i B polje u istom smjeru (ubrzana spirala)",
        "E": np.array([0.0, 0.0, 0.2]),
        "B": np.array([0.0, 0.0, 2.0])
    },
    {
        "naslov": "3. E polje okomito na B polje",
        "E": np.array([0.3, 0.0, 0.0]),
        "B": np.array([0.0, 0.0, 2.0])
    }
]

#crta po jedan graf za svaki scenarij
for podaci in scenariji:
    ax = plt.axes(projection='3d') #AI, 3d graf
    
    #elektron
    ex, ey, ez = simulacijaGibanja(-1.0, masa_cestice, podaci["E"], podaci["B"], vrijeme_trajanja, dt)
    ax.plot(ex, ey, ez, label="Elektron", color="blue")
    
    #pozitron
    px, py, pz = simulacijaGibanja(1.0, masa_cestice, podaci["E"], podaci["B"], vrijeme_trajanja, dt)
    ax.plot(px, py, pz, label="Pozitron", color="red")
    
    ax.set_title(podaci["naslov"])
    ax.set_xlabel('X os [m]')
    ax.set_ylabel('Y os [m]')
    ax.set_zlabel('Z os [m]')
    ax.legend()
    plt.show()