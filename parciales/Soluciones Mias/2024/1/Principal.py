import random
from Clase import *
import pickle
import os.path
import os

def validar():
    inf = int(input('Ingresa un numero:'))
    while not inf >0 :
        inf = int(input('Ingresa un numero:'))
    return inf

def cargar(v):
    x = validar()
    Names = ['Sabina', 'Alejo', 'Pepe', 'Jesus', 'Shado', 'Garden', 'p', "Carlos", "Ana", "José", "María", "Pedro",
             "Belén", "Martín", "Soledad"]
    for i in range(x):
        ide = random.randint(0,100000000)
        Nombre = random.choice(Names)
        edad = random.randint(12,17)
        nivel = random.randint(0,2)
        Monto = round(random.uniform(0,100000000),2)
        x = Equipo(ide,Nombre,edad,nivel,Monto)
        add_in_ord(v,x)
    return v

def add_in_ord(v,x):
    n = len(v)
    isq,der = 0,n-1
    pos = n

    while isq <= der:
        c=(isq+der)//2
        if x.Nombre == v[c].Nombre:
            pos = c
            break
        if x.Nombre > v[c].Nombre:
            isq = c+1
        else:
            der = c-1
    if isq > der:
        pos = isq

    v[pos:pos] = [x]


def mostrar(v):
    nivele = ['Bajo', 'Intermedio', 'Avanzado']

    for i in range(len(v)):
        print(v[i].ide, v[i].Nombre, v[i].edad,nivele[v[i].nivel], v[i].Monto)



def Acumulador(v):
    matriz = [[0] * 3 for _ in range(6)]

    for k in range(len(v)):
        c = v[k].edad - 12
        f = v[k].nivel
        matriz[c][f] += v[k].Monto

    nivele = ['Bajo', 'Intermedio', 'Avanzado']

    for i in range(6):
        for j in range(3):
            print('Edad:', i + 12,
                  'Nivel:', nivele[j],
                  'Monto:', matriz[i][j])

    e = int(input('Ingrese la edad: '))

    total = 0
    f = e - 12

    for c in range(3):
        total += matriz[f][c]

    print('Monto total para la edad', e, ':', total)

    return matriz

def Writen(v):
    m = open('equipo','wb')
    i1,i2 = int(input('ingrese Ide de equipo,menor')),int(input('ingrese Ide de equipo,mayor'))
    for i in range(len(v)):
        if i1<=v[i].ide<=i2:
            pickle.dump(v[i],m)
    m.close()



def leer():
    archivo = 'equipo'
    if not os.path.exists(archivo):
        print('CREA EL ARCHIVO')
        return None
    m = open(archivo,'rb')
    t = os.path.getsize(archivo)
    while m.tell() < t:
        r =pickle.load(m)
    m.close()

    print('Finalise')

def main ():
    menu()


def menu():
    x = -3
    v = []
    while x != 0 :
        print('1\tCargar')
        print('2\tMostrar')
        print('3\tAcumular')
        print('4\tCargar Texto')
        print('5\tLeer Texto')
        print('0\tCargar')
        x = int(input('Ingrese la opcion:'))
        if x == 1 and not v:
            v=cargar(v)
        if v :
            if x == 2:
                mostrar(v)
            elif x == 3:
                Acumulador(v)
            elif x == 4:
                Writen(v)
            elif x == 5:
                l = leer()





if __name__ == '__main__':
    main()