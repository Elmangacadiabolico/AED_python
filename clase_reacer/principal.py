import os.path
import random
import pickle
from clase import *

def menu():
    print("-"*100)
    print("1. Cargar de tratamientos (con inserción ordenada)")
    print("2. Cargar de afiliados (con inserción ordenada)")
    print("3. Conteo o Búsqueda (según sea requerido)")
    print("6. Salir del programa.")
    return int(input("Ingrese la opción: "))



def validar(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio mayor a ' + str(inf) + '... Cargue de nuevo: '))
    return n

def montos():

    pass

def carga_de_datos(fd,v):
    pass

def lectura(fd):
    v = []
    m = open(fd, 'rt')
    m.readline()
    for i in m:
        i = i.strip()
        if i:
            v.append(i.split(','))
    m.close()
    return v


def cargar_afiliados(fd2,v):
    datos = lectura(fd2)

    for i in datos:
        cob = Cobertura(int(i[0]),int(i[1]),int(i[2]),int(i[3]))
        add_in_orden(v,cob)
    return v

def carga_tratamientos(fd,v):
    datos = lectura(fd)

    for i in datos:
        trat = Tratamientos(int(i[0]),int(i[1]),int(i[2]),int(i[3]),float(i[4]),(i[5]),int(i[6]))
        add_in_orden(v,trat)
    return v

def add_in_orden(v, datos):
    isq, der = 0, len(v) - 1
    pos = len(v)
    while isq <= der:
        c = (isq + der) // 2
        if v[c].dni == datos.dni:
            pos = c
            break
        if v[c].dni > datos.dni:
            der = c - 1
        else:
            isq = c + 1
    if isq > der:
        pos = isq
    v[pos:pos] = [datos]
    return v


def mostrar(vt,vf):
    for i in vt:
        print(i)
    for j in vf:
        print(j)

def main():
    fd = "tratamientos.csv"
    fd2 = 'coberturas.csv'
    vf = []
    vt = []
    op = -1
    eop2 = eop1 = False
    while op != 6:
        op = menu()
        if op == 1 and os.path.exists(fd):
            vt = carga_tratamientos(fd, [])
            eop1 = True

        elif op == 2:
            if os.path.exists(fd2) and vt:
                eop2 = True
                vf = cargar_afiliados(fd2, [])
            else:
                print("el vector no fue cargado todavía...")
        elif op == 3:
            if (vt or vf) and eop1 and eop2:
                mostrar(vt, vf)
            else:
                print("El vector no fue cargado todavía...")


if __name__ == "__main__":
    main()