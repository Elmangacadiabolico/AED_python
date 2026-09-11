import random
n = 27000
random.seed(37)

Pc = i1_a= i1_b=i1_c= i2= Count = i3=may=i4=0
may = None


for i in range (n):
    NumeRandom = random.randint(-20000, 30000 )
    Pc += NumeRandom
    #i1
    if -20000 <= NumeRandom < -5000:
        i1_a += 1
    if -5000 <= NumeRandom < 15000:
        i1_b += 1
    if NumeRandom >= 15000 and (NumeRandom%9)==0:
        i1_c += 1
    #I2
    String_stg = str(NumeRandom % 10)
    if NumeRandom >= 1000 and String_stg in'46' :
        i2 += NumeRandom
        Count += 1
    #i3
    if NumeRandom > 0 and (NumeRandom%2)!=0 and (NumeRandom%10) != 1:
        if may is None:
            may = NumeRandom
        elif NumeRandom > may:
             may = NumeRandom
    i3 = may
    #i4
    if NumeRandom % 7 == 0:
       i4 += 1


prom = (i2//Count)
porcentaje = (i4*100)//n
print(i1_a)
print(i1_b)
print(i1_c)
print(prom)
print(i3)
print(porcentaje)
