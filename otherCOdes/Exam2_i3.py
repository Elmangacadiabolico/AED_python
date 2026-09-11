import random
N = 25000
ct = N3= n5_3= nd3_5 =count=I3sum=0
random.seed(20220512)
mayor = None

for i in range (N):
    NR = random.randint(1,45000 )
    ct += NR
    #consigna 1
    if(NR % 3) == 0:
        N3 += 1
    if((NR % 5) == 0) and ((NR % 3) != 0):
        n5_3 += 1
    if NR % 3 != 0 and NR % 5 != 0:
        nd3_5 += 1
    #consigna 2
    ste = str(NR)[0]
    if ste[0] in '1':
        if mayor is None:
            mayor = NR
        elif NR > mayor:
            mayor = NR
    #consigna 3
    if NR % 2 == 0 and NR % 11 == 0:
        count+=1
        I3sum += NR


prom = I3sum//count
#consigna 4
por1= (N3 * 100)//N
por2= (n5_3 * 100)//N
por3= (nd3_5 * 100)//N



print(N3)
print(n5_3)
print(nd3_5)
print(mayor)
print(prom)
print(por1)
print(por2)
print(por3)
