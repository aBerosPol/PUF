#a

a = 5.0
b = 4.935
print (f"{a} - {b} = {a - b} \n Razlog zasto Python ispisuje ovo rjesenje umjesto 0.065 je sto racuna u binarnom zapisu, a 0.065 se ne moze tocno zapisati u binarnom sustavu. Pri prebacaju iz dekadskog u binarni sustav dolazi do ove pogreske zbog gubitka preciznosti.")

#b
b1 = 0.1
b2 = 0.2
b3 = 0.3
if b1 + b2 == b3:
    print (f"{b1} + {b2} = {b3}")
else:
    print(f"{b1} + {b2} = {b1 + b2} \n Razlog zasto Python ispisuje ovo rjesenje umjesto tocnog rjesenja je sto racuna u binarnom zapisu, a tocno rjesenje se ne moze tocno zapisati u binarnom sustavu. Pri prebacaju iz dekadskog u binarni sustav dolazi do ove pogreske zbog gubitka preciznosti.")