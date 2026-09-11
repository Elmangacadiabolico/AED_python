import random

N = 20000
random.seed(49)
m1 = m2 = m3 = 0
mayor = 0
pares_menores = 0
control = 0

for i in range(N):
    num = random.randint(1, 45000)
    control += num
    if num % 5 == 0:
        m1 += 1
    if num % 7 == 0:
        m2 += 1
    if num % 9 == 0:
        m3 += 1

    ultimo = num % 10
    if 5 <= ultimo <= 8:
        if num > mayor:
            mayor = num
    if num % 2 == 0 and num < 15000:
        pares_menores += 1

# porcentaje
porcentaje = (pares_menores * 100) // N


print("Multiplos de 5:", m1)
print("Multiplos de 7:", m2)
print("Multiplos de 9:", m3)
print("Mayor con último dígito entre 5 y 8:", mayor)
print("Pares menores a 15000:", pares_menores)
print("Porcentaje:", porcentaje)