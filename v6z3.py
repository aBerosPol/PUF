import numpy as numpy

dijametri = numpy.array([
    [19.98, 20.18, 20.10, 20.08, 19.74],
    [19.92, 19.82, 19.96, 19.98, 19.88],
    [24.96, 24.98, 24.98, 24.92, 24.94]
    ])

duljine = numpy.array ([
    [49.80, 49.00, 50.48, 49.80, 49.96],
    [52.56, 52.50, 52.62, 52.58, 52.54],
    [55.34, 55.40, 55.30, 55.44, 55.48]
    ])

mase = numpy.array ([
    [138.92, 138.98, 139.20, 138.90, 138.92],
    [128.65, 128.60, 128.65, 128.35, 128.50],
    [71.89, 71.90, 71.79, 71.85, 71.70]
])

def srednjaVrijednost_standardnaDevijacija (mjerenja):
    #srednja vrijednost
    sum1 = 0
    for i in range (len(mjerenja)):
        sum1 += mjerenja [i]
    avg = sum1 / len(mjerenja)
    
    #standardna devijacija
    sum2 = 0
    for i in range (len(mjerenja)):
        sum2 += (mjerenja[i] - avg)**2
    stDev = (sum2 / (len(mjerenja) * (len(mjerenja) - 1)))**0.5    

    return avg, stDev



def volumenValjka (R, L): #prima cm, vraca cm^(3)
    R = R / 10
    L = L / 10
    V = (R**2) * numpy.pi * L
    return V

def sigmaVolumena (R, sigmaR, L, sigmaL):
    brojnik = (2 * R * numpy.pi * L * sigmaR)**2

def gustoca(m, V):
    return m / V


def sigmaGustoce(m, sigmaM, V, sigmaV):

    rho = gustoca(m, V)

    term_m = (sigmaM / m) ** 2 #pogreska u mjerenju, ova dva reda AI
    term_V = (sigmaV / V) ** 2

    return rho * numpy.sqrt(term_m + term_V)

#AI
def sigma_volumena(R, sigmaR, L, sigmaL):
    V = volumenValjka(R, L)
    term_R = (2 * sigmaR / R)**2
    term_L = (sigmaL / L)**2
    return V * numpy.sqrt(term_R + term_L)


for i in range(len(dijametri)):
    radijusi = dijametri[i] / 2
    R_avg, sigmaR = srednjaVrijednost_standardnaDevijacija(radijusi)
    L_avg, sigmaL = srednjaVrijednost_standardnaDevijacija(duljine[i])
    m_avg, sigmaM = srednjaVrijednost_standardnaDevijacija(mase[i])
    
    V = volumenValjka(R_avg, L_avg)
    sV = sigma_volumena(R_avg, sigmaR, L_avg, sigmaL)
    rho = gustoca(m_avg, V)
    sigmaRho = sigmaGustoce(m_avg, sigmaM, V, sV)
    
    print(f"\n--- Valjak {i+1} ---")
    # Ispis u znanstvenom zapisu (.4e)
    print(f"Volumen V: {V:.4e} cm3")
    print(f"Sigma volumena: {sV:.4e} cm3")
    print(f"Rezultat: ({V:.3e} +/- {sV:.3e}) cm3")
    print(f"Gustoća: ({rho:.3e} +/- {sigmaRho:.3e}) g/cm3")