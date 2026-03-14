def pravac (x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    l = y1 - (k * x1)
    print (f"Jednadzba tvog pravca je y = {k} * x + {l}")

x1 = float(input("Unesi x1 koordinatu. "))
y1 = float(input("Unesi y2 koordinatu. "))
x2 = float(input("Unesi x2 koordinatu. "))
y2 = float(input("Unesi y2 koordinatu. "))

pravac (x1, y1, x2, y2)