import random
from Registro import *

def main():
    x = -3
    v =[]

    while x != 5:
        print("1.\tCarga")
        print("2.\tMostrar")
        print("3.\tContador de taxis")
        print("4.\tBusqueda de DNI")
        print("5.\tFinalizar programa")
        x = int(input('Ingrese la opcion'))
        if x == 1:
            v=cargar(v)
        if v:
            if x == 2:
                mostrar(v)
            elif x == 3:
                contador(v)
            elif x == 4:
                y =busqueda(v)
                print(y)
        else:
            print('debe de cargar primero los datos')

def cargar(v):
    x = verificar(0)
    v = [None]*x
    for i in range(len(v)):
        ide = random.randint(0,80000)
        DNI = random.randint(100, 1000000000)
        marca = random.randint(1,20)
        tarifa = random.randint(0,300)
        v[i] = taxis(ide,DNI,marca,tarifa)
        print(v[i])
    return v
def mostrar(x):
    cc = 0
    v = orde(x)
    i1 = int(input('Ingrese valor min'))
    i2 = int(input('ingrese valor max'))
    for i in range(len(v)):
        if i1 <= v[i].tarifa <= i2:
            cc+=1
            print(v[i])
    print(cc,"cantidad de taxis que recorieron",i1,"km",i2,"km")



def verificar(min):
    if min == 0:
        while min == 0:
            min = int(input('Ingrese un valor mayor a 0'))
            print(min)
    return min


def orde(v):
    n =len(v)
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i].ide > v[j].ide:
                v[i].ide,v[j].ide = v[j].ide,v[i].ide
    return v

def contador(v):
    av = [0] *20
    for i in range(20):
        ind = v[i].marca - 1
        av[ind] += 1
    for k in range(20):
        if av[k] != 0:
            print("Marca:",k+1,"taxis:",v[k])


def busqueda(v):
    x = int(input('Ingrese el DNI a buscar'))
    for i in range(len(v)):
        if x == v[i].DNI:
            v[i].tarifa = v[i].tarifa-(12/100)
            return print(v[i])





if __name__=='__main__':
    main()