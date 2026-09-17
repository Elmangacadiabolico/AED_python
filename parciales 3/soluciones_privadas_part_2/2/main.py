import random
from Registro import *
def main():
    v = []
    x = -3
    while x != 0:
        print('1.\tCargar')
        print('2.\tMostrar')
        print('3.\tConteo')
        print('4.\tCargar')
        print('0.\tBusqueda')
        x = int(input('ingrese un valor para la opcion'))

        if x == 1:
            v=cargar(v)
        if v:
            if x == 2:
                mostrar(v)
            elif x == 3:
                op3(v)
            elif x == 4:
                busqueda(v)
        else:
            print('Error Critico faltal!\nCarge los datos putosssss!!!')

def cargar(v):
    x = verificacion(0)
    v = [None] * x
    for i in range(len(v)):
        ide = random.randint(0,1000)
        diametro = random.randint(0,100)
        tipo = random.randint(1,20)
        cant = random.randint(0,100)
        ingifugo = random.randint(1,2)
        v[i] = productos_pvc(ide,diametro,tipo,cant,ingifugo)
        print(v[i])
    return v

def op3(v):
    x = int(input('valor  a'))
    Nv = [0] * 20
    for i in range(len(v)):
        p = v[i].tipo -1
        Nv[p] += 1
    for k in range(len(Nv)):
        if Nv[k] >= x:
            print('valores de k',k +1,Nv[k])

def verificacion(l):
    x = int(input('ingrese un valor'))
    while  l > x:
        x = int(input('ingrese un valor mayor a 0'))
    return x

def mostrar(v):
    v = ordenar(v)
    c = 0
    for i in range(len(v)):
        if v[i].ignifugo == 1:
            c += v[i].diametro
            print(v[i])
    if c == 0:
        return print('Error Critico faltal!')
    else:
        promt = round(c/len(v),2)
        print("el promedio por diametro:",promt)


def ordenar(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i].diametro > v[j].diametro:
                v[i] , v[j] = v[j] , v[i]
    return v

def busqueda(v):
    x = int(input('ingrese el Id a buscar'))
    for i in range (len(v)):
        if x == v[i].ide:
            return print("se encontro..\tsu uso es:",v[i].tipo,"diametro:",v[i].diametro)
    else:
        return print('Error Critico faltal!')

if __name__=='__main__':
    main()