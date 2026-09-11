import random
N = 20000
random.seed(49)

#lets
ct = i1_A =i1_b =i1_c =i3=i2=Test =  0
may = None
for i in range(N):
    NumerGenerados = random.randint(1,45000)
    ct += NumerGenerados
    #A1
    if NumerGenerados % 5 == 0:
        i1_A += 1

    if NumerGenerados % 7 == 0:
        i1_b += 1
    if NumerGenerados % 9 == 0:
        i1_c += 1
    #2
    if 5 <= (NumerGenerados % 10) <= 8:
        if may is None:
            may = NumerGenerados
        elif NumerGenerados > may:
            may = NumerGenerados



    #3
    if NumerGenerados % 2 == 0 and NumerGenerados < 15000:
        i3 += 1

porc= (i3*100)//N
print(i1_A, i1_b, i1_c)
print(may)
print(i3)
print(porc)