import random
N = 25000

random.seed(20220512)
Nm3 = Nm5 = N3yN5 = count= NPar_11 = mayor=  0
for i in range(N):
    NR = random.randint(1, 45000)
#act 1
    if (NR % 3) == 0:
        Nm3+=1
    elif (NR % 5) ==0 and (NR % 3) != 0:
        Nm5+=1

    if (NR % 3) != 0 and (NR % 5) != 0:
        N3yN5 +=1
#act 2

    if str(NR)[0] == "1":
        if NR > mayor:
            mayor = NR
#act3
    if (NR % 2) == 0 and (NR % 11) == 0:
        count +=1
        NPar_11 += NR
       # prom = NPar_11 // count
    #chat  iA help
    if count != 0:
        prom = NPar_11 // count
    else:
        prom = 0

#act4
p3 = (Nm3*100) // N
p5 = (Nm5*100) // N
pN3yN5 = (N3yN5*100) // N


#promedio  es la suma de todo sus numerous / la cantidad de suma
print(Nm3)
print(Nm5)
print(N3yN5)
print("a",mayor)
print(prom)
print(p3)
print(p5)
print(pN3yN5)