from Registro import *
import random

def main():
    v =[]
    n = -3
    while n != 5:
        print('1.\tCargar')
        print('2.\tMostrar')
        print('3.\tCantidad de productos')
        print('4.\tbusqueda')
        print('5.\texit')
        n = int(input('ingrese la opcion a elegir:'))

        if n == 1:
            v = cargar(v)
        if v:
            if n == 2:
                Mostrar(v)
            elif n==3:
                conteo(v)
            elif n==4:
                pass
        else:
            print('Error, Carge porfacor los datos')




def cargar(v):
    x = verificar(0)
    v = [None] * x
    for i in range(len(v)):
        codigo = random.randint(0,3000)
        descripcion = random.randint(1,30000)
        tipo = random.randint(1,30)
        calorias = random.randint(0,900)
        precio = round(random.uniform(0.50,1000),2)
        v[i]= productos(codigo,descripcion,calorias,tipo,precio)
        print(v[i])
    return v
def Mostrar(v):
    c = 0
    v = ord(v)
    for i in range(len(v)):
        c += v[i].calorias
        print(v[i])
    prom = round(c/len(v),2)
    print('el promedio es:',prom)



def verificar(x):
    x = int(input('ingrese un valor mayor a 0:'))
    while x < 0 :
        x = int(input('ingrese un valor mayor a 0:'))
    return x


def ord(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i].calorias > v[j].calorias:
                v[i],v[j] = v[j],v[i]
    else:
        return v


def conteo(v):
    cv =[0] * 30
    for i in range(30):
        p = v[i].tipos -1
        cv[p] += 1
        print(cv[i])



if __name__ == '__main__':
    main()