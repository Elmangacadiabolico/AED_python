from modulo2 import *
import random

def validar(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio mayor a ' + str(inf) + '... Cargue de nuevo: '))
    return n

def op1(v):
    x = validar(0)
    v = [None] * x
    nombre = ['Amburgesa','lomito','helado','pizza','ensalada']
    for i in range(len(v)):
        id = random.randint(300, 1000000)
        caracters = random.choice(nombre),str(i)
        tipo = random.randint(1,30)
        calorias = round(random.uniform(1,500),2)
        precio = round(random.uniform(1,50),2)
        v[i]= Productos(id,caracters,calorias,tipo,precio)

    return v
def ord(v):
    l = len(v)
    for i in range(l-1):
        for j in range(i+1,l):
            if v[i].calorias > v[j].calorias:
                v[i].calorias,v[j].calorias = v[j].calorias,v[i].calorias
    return v

def ord2(v):
    l = len(v)
    for i in range(l-1):
        for j in range(i+1,l):
            if v[i].id > v[j].id:
                v[i].id,v[j].id = v[j].id,v[i].id
    return v

def op2(v):
    c = 0
    v = ord(v)

    for n in range(len(v)):
        c += v[n].calorias
        print(v[n])
    prom = round((c/len(v)),2)
    print("el promedio:",prom)
    return v,prom

def op3(v):
    v2 =[0] * 30
    for i in range(len(v)):
        p = v[i].Tipo -1
        v2[p] += 1
    print(v2)

def op4(v):
    x = int(input('Ingrese la Id a buscar'))
    n = len(v)
    v = ord2(v)
    izq = 0
    der = n-1
    while izq <= der:
        c = (izq+der)//2
        if x == v[c].id:
            print("Encontrado:")
            print("Descripcion del producto:",v[c].id, v[c].caracts,v[c].Tipo,v[c].precion)
            return c
        elif x > v[c].id:
            izq = c+ 1
        else:
            der = c - 1
    return -1

def main():
    v =[]
    x = -1
    while x != 0:
        print('Cargarn 1')
        print('mostrar 2')
        print('tipo de producto 3')
        print('busqueda 4')
        print('salida 0')
        x = int(input('Ingrese su elecion'))

        if x == 1:
            v = op1(v)
        if v:
            if x == 2:
                op2(v)
            elif x == 3:
                op3(v)
            elif x == 4:
                op4(v)


if __name__ == '__main__':
    main()