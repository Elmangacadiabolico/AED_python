from Registro import *
import random

def main():
    v=[]
    x = -3
    while x != 0:
        print('1\tCargar datos')
        print('2\tMostrar datos')
        print('3\tCantidad de pinturas')
        print('4\tbusqueda por codigo')
        print('0\tExit')
        x =int(input('ingrese el numero para selecionar una opcion'))

        if x == 1:
            v =cargar(v)
        if v:
            if x == 2:
                mostrar(v)
            elif x == 3:
                opc3(v)
            elif x == 4:
                op4(v)

def verificar(x):
    if x == 0:
        x = int(input('ingrese el numero de pinturas mayor a 0'))
    return x


def cargar(v):
    x = verificar(0)
    v = [None] * x
    for i in range(len(v)):
        color= random.randint(0,255)
        tipo = random.randint(1,10)
        rendimiento=random.randint(50,10000)
        precio=random.randint(0,1000)
        v[i]= pintura(color,tipo,rendimiento,precio)
        print(v[i])
    return v

def mostrar(v):
    cc = 0
    v = ord(v)
    p = int(input('ingrese un precio aceptable'))
    r = int(input('ingrese el rendimiento aceptable'))

    for i in range (len(v)):
        if v[i].precio < p and v[i].rendimiento > r:
            cc += 1
            print(v[i])
    print("cantidad de resultados encontrados:",cc)

def opc3(v):
    Nv = [0] * 10
    for i in range (10):
        ind = v[i].tipo -1
        Nv[ind] += 1
        print(Nv[i])


def op4(v):
    x = int(input('ingrece el color para busacrlo'))
    for i in range (len(v)):
        if x == v[i].color:
            v[i].rendimiento = int(input('ingrese el nuevo rendimiento:'))
            return print(v[i])

    return print('no se encontro ningun valor coincidente')
def ord(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i].precio > v[j].precio:
                v[i],v[j] = v[j],v[i]
        print(v[i])
    return v


if __name__ == '__main__':
    main()