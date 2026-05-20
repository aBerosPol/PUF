import numpy as numpy

#trazi srednji radijus i sigmaR, srednju duljinu i sigmaL, srednju masu i sigmaM

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
    

print (len(dijametri))
for lista in dijametri:
    print(len(lista))

valjak1 = []
valjak2 = []
valjak3 = []


#AI:
imena_valjaka = ["Valjak 1", "Valjak 2", "Valjak 3"]

for i in range(len(dijametri)):
    radijusi = dijametri[i] / 2
    R_avg, sigmaR = srednjaVrijednost_standardnaDevijacija(radijusi)
    
    L_avg, sigmaL = srednjaVrijednost_standardnaDevijacija(duljine[i])
    
    M_avg, sigmaM = srednjaVrijednost_standardnaDevijacija(mase[i])
    
    print(f"\n--- {imena_valjaka[i]} ---")
    print(f"Radijus: {R_avg:.4f} +/- {sigmaR:.4f}")
    print(f"Duljina: {L_avg:.4f} +/- {sigmaL:.4f}")
    print(f"Masa:    {M_avg:.4f} +/- {sigmaM:.4f}")