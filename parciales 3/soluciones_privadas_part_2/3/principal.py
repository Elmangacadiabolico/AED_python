import random
from Registro import *

def main():
    v =[]
    x = -5
    while x != 0:
        print('1.\tCargar datos')
        print('2.\tMostrar datos')
        print('3.\tContar datos')
        print('4.\tBuscar DNI')
        print('0.\tSalida del programa')
        x = int(input('ingrese un numero para selecionar la opcion.\t'))

        if x == 1:
            v = cargar(v)
        if v:
            if x == 2:
                Mostrar(v)
            elif x == 3:
                contar(v)
            elif x == 4:
                busqueda(v)


def cargar(v):
    x = verificado(0)
    v = [None] * x

    for i in range(len(v)):
        ide = random.randint(0,10000)
        DNI = random.randint(0, 1000000)
        modelo = random.randint(1, 20)
        tarifa = random.randint(0, 100000)
        v[i] = taxi(ide,DNI,modelo,tarifa)
        print(v[i])
    return v

def Mostrar(v):
    cc=0
    v = ordenar(v)
    i1= int(input('ingrese un menor'))
    i2= int(input('ingrese un valor mayor'))
    for i in range(len(v)):
        if i1 <= v[i].tarifa <= i2:
            cc+=1
            print(v[i])
    print("es la cantidad de taxis",cc,"dentro del intervalor",i1,":",i2)


def verificado(inf):
    x = int(input('ingrese un valor'))
    while x < inf:
        x = int(input('ingrese un valor mayor a 0'))
    return x

def ordenar(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i].ide > v[j].ide:
                v[i],v[j] = v[j],v[i]
    return v

def contar(v):
    Nv =[0] * 20
    for i in range(len(v)):
        ide = v[i].modelo -1
        Nv[ide] += 1

    for k in range(len(Nv)):
        if Nv[k] != 0:
            print("modelo:",k,"taxi",Nv[k])
def busqueda(v):
    x = int(input('Carge el DNI para buscar'))
    for i in range(len(v)):
        if x == v[i].DNI:
            v[i].tarifa = round(v[i].tarifa -(v[i].tarifa *(15/100)),2)
            return print(v[i])
    return print('No se encontro el DNI o Ocurrio un Error')

if __name__ == '__main__':
    main()