import random
NR = 50
random.seed(332)
cN = numerM0_12= Numero12_17 = NumerImpar_7=Num217 = Rare =0

for i in range (NR):
    NG = random.randint(-500,0)
    cN += NG
    #ACT 1
    if 0 <= (NG**2) < 120000:
        numerM0_12 += 1
    if 120000 <= (NG**2) < 170000:
        Numero12_17 += 1
    if (NG**2) >= 170000 and ((NG**2) % 2) != 0 and ((NG**2) % 7) == 0:
        NumerImpar_7 += 1

    #end ACT 1
    #act2
    if (NG % 7) == 0 and (NG % 3) == 0 or(NG % 11) == 0:
        Rare +=1
    #end act2
    #act3
    if ((NG**2) % 2) == 0 and (NG) >= 170000:
        Num217 +=1







print(cN)
print(numerM0_12)
print(Numero12_17)
print(NumerImpar_7)
print(Rare)
print(Num217)