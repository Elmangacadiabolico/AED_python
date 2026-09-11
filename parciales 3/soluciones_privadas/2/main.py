from clase import *
import random

def main():
    v = []
    x = -3
    while x != 0:
        print('1.\tCarga')
        print('2.\tMostrar')
        print('3.\tCantidad de tubos fabricados')
        print('4.\tbusqueda de tubo por codigo')
        print('0.\tbusqueda de tubo por codigo')
        x = int(input('ingrese la opcion'))

        if x == 1:
            v = carga(v)
        if v:
            if x == 2:
                op2(v)
            elif x == 3:
                op3(v)
            elif x== 4:
                buscar(v)

def carga(v):
    n = int(input('ingrese un valor mayor a 0'))
    v = [None] * n
    for i in range(len(v)):
        ide = random.randint(0 ,10000)
        diametro = random.randint(1, 1000)
        uso = random.randint(1,20)
        gramo = random.randint(0,5000)
        ignifugo = random.randint(1,2)
        v[i] = producion_pvc(ide,diametro,uso,gramo,ignifugo)
        print(v[i])
    return v


def op2(v):
    x = cc=0
    v = ord(v)
    for i in range(len(v)):
        if v[i].ignifugo == 1:
            x +=  v[i].gramos
            cc  +=1
            print(v[i])
    prom=x//cc
    print(prom,"gramos\tUsados para su fabricación")

def op3(v):
    n = len(v)
    c = [0] * 20
    for i in range(n):
        ind = v[i].uso -1
        c[ind] += 1
    x = int(input('carge el valor max a moostrar'))
    for j in range(20):
        if c[j] >= x:
            print("codigo:",j+1,c[j],"se encontro")



def ord(v):
    n = len(v)
    for i in range(n-1):
        for j in range(n+i,n):
            if v[i].diametro < v[j].diametro:
                v[i].diametro,v[j].diametro = v[j].diametro,v[i].diametro
    return v

def buscar(v):
    iden = int(input('ingrese el codigo de producto:'))
    for i in range(len(v)):
        if iden == v[i].ide:
            return print(v[i].uso,"su diametro:",v[i].diametro)
    else:
        print('no se encontro ningun producto')





if __name__=='__main__':
    main()