import random
random.seed(9182)
N = 24000

Control =i1_a = i1_b= i1_c=i2_a= X =i3= i4= 0
men = None
for i in range(N):
    NumerGR =random.randint(-45000, 25000)
    Control += NumerGR
    Y1 = NumerGR**3

    #A1
    if -1000000000 <= NumerGR < 0:
        i1_a += 1
    if 0 <= NumerGR < 900000000:
        i1_b +=1
    if NumerGR >= 900000000 and (NumerGR % 9) == 0:
        i1_c += 1
    #A2
    if (NumerGR < 0 and (NumerGR % 5) == 0 )or(NumerGR > 0 and  str(NumerGR % 2) == 0 ):
        i2_a += 1
    #A3
    if NumerGR >0 and (Y1 % 2) == 0:
        X += NumerGR
        if X % 7 == 0:
            i3 += 1
            if men is None:
                men = NumerGR
            elif NumerGR < men:
                men = NumerGR
    #A4
    if NumerGR < 0 and( str(NumerGR).ljust == 4 and NumerGR % 13 == 0 or NumerGR % 17 == 0):
        i4 += 1






por = (i2_a*100)//N
print(Control)
print("toda Actividad 1: ",i1_a ,i1_b,i1_c)
print("all ACT 2:",i2_a,"y su promedio es",por)
print("A3:", men)
print("A4",i4)


