import random
random.seed(8665)
NR=16000
ct = NM = N12 = NM0 = Cont = mkm = NIP =  NMD= 0
menor1 = None
for i  in range(NR):
    Numer=random.randint(-1000,18000)
    ct += Numer
#actividad 1
    if Numer <= 3000:
        NM += 1
    if 3000 < Numer < 12000:
        N12 +=Numer
    if Numer >= 12000 and (Numer % 3 )!= 0 and (Numer % 4) != 0:
        NMD += 1
#Actividad 2
    if Numer >= 0 and (Numer % 8) == 0:
        Cont +=1
        NM0 +=Numer

#Actividad 3
    if 5000 <= Numer <= 13000 and Numer % 2 == 0:
        if menor1 is None or Numer < menor1:
            menor1 = Numer
#ACT 4
    if Numer >= 0 and (Numer % 3)!= 0:
        NIP +=1

promedio = NM0 // Cont
porcentaje = (NIP * 100)//NR


print(NM) #X
print(N12)
print(NMD)
print(NM0)
print(promedio)
print(menor1)
print(porcentaje)


