import random
N = 27000
random.seed(37)

i1_A =i1_b= i1_c = i2 =Count= i3 =0
May = None
for i in range(N):
    randoNumbers = random.randint(-20000, 30000 )
    #A!
    if -20000 <= randoNumbers < -5000:
        i1_A += 1
    if -5000 <= randoNumbers < 15000:
        i1_b +=1
    if randoNumbers >= 15000 and (randoNumbers % 9) == 0:
        i1_c += 1
    #A2
    if randoNumbers >= 1000  and  str(randoNumbers % 10) in '4 6 ':
        Count +=1
        i2 += randoNumbers
    #A3
    if randoNumbers > 0 and randoNumbers % 2 != 0 and  str(randoNumbers % 10) != 1:
        if May is None:
            May = randoNumbers
        elif randoNumbers > May:
            May = randoNumbers
    #A4
    if randoNumbers % 7 == 0:
        i3 += 1


prom = (i2//Count)
porc= (i3*100)//N
print(i1_A, i1_b, i1_c)
print("act2",prom)
print(May)
print(porc)
