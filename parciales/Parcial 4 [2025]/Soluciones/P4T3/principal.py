import os.path
import pickle
import random

# Use la forma de importación que prefiera.
# Comente una y descomente la otra, a su gusto.
# import clase
from clase import Equipo


# Muestra las opciones, y carga y retorna la que elija el usuario.
def menu():
    print("1. Cargar (con inserción ordenada")
    print("2. Mostrar (de acuerdo a lo requerido")
    print("3. Conteo o Búsqueda (según sea requerido)")
    print("4. Generar archivo binario (de acuerdo a lo requerido")
    print("5. Mostrar archivo binario (de acuerdo a lo requerido")
    print("6. Salir del programa.")
    return int(input("Ingrese la opción: "))


# Carga y retorna un número, validando que sea mayor al valor inf que entra como parámetro.
def validar(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio mayor a ' + str(inf) + '... Cargue de nuevo: '))
    return n


def generar_aleatorio():
    nombres = (
        "Alpha Strike", "Crimson Vipers", "Shadow Core", "Echo Squad", "Team Hydra", "Nova Aim",
        "Valor Kings", "Phoenix Rising", "Oblivion", "Recoil Nation", "Blue Fang", "Silent Storm",
        "Tactical Edge", "Ghost Ops", "Pulse Unit", "Astra Elite", "Prime Strike", "Midnight Crew",
        "Iron Wolves", "Nemesis", "Chaos Unit", "Rogue Line", "Delta Force", "Spectre", "Zero Hour"
    )

    nombre = random.choice(nombres)
    jugadores = random.randint(5, 8)
    rango = random.randint(1, 8)
    puntaje = random.randint(100, 1000)
    region = random.randint(1, 4)
    return Equipo(nombre, jugadores, rango, puntaje, region)


def cargar_en_rango(lim_inf, lim_sup, mensaje='Ingrese un valor'):
    n = int(input(mensaje))
    while n < lim_inf or n > lim_sup:
        n = int(input(f'Error. Se espera un valor entre {lim_inf} y {lim_sup}. {mensaje}'))
    return n


# Función principal o de arranque.
def add_in_order(v, car):
    n = pos = len(v)
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2
        if car.nombre == v[c].nombre:
            pos = c
            break

        if car.nombre < v[c].nombre:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [car]


def cargar_equipos(n):
    v = []
    for i in range(n):
        c = generar_aleatorio()
        add_in_order(v, c)
    return v


def mostrar_equipos(v, r1):
    cont = 0

    for c in v:
        print(c)
        if c.rango == r1:
            cont += 1

    print(f'r.2: {cont}')


def contar_equipos(v):
    mat = [[0] * 4 for i in range(8)]

    for e in v:
        f = e.rango - 1
        c = e.region - 1
        mat[f][c] += 1

    return mat


def mostrar_matriz(m):
    filas, columnas = len(m), len(m[0])

    for f in range(filas):
        for c in range(columnas):
            if m[f][c] > 0:
                print(f'Rango {f + 1}, Región {c + 1}, Cantidad: {m[f][c]}')


def generar_archivo(fd, v, puntaje):
    m = open(fd, 'wb')

    for e in v:
        if e.puntaje >= puntaje:
            pickle.dump(e, m)
    m.close()


def mostrar_archivo(fd):
    acum = cont = 0
    tam = os.path.getsize(fd)
    m = open(fd, 'rb')

    while m.tell() < tam:
        e = pickle.load(m)
        print(e)
        if e.rango == 6:
            acum += e.puntaje
            cont += 1

    m.close()
    promedio = 0
    if cont > 0:
        promedio = acum / cont
    print(f'r5.1: {promedio}')


def main():
    random.seed(13715)
    fd = "archivo.dat"
    v = []
    op = -1
    while op != 6:
        op = menu()
        if op == 1:
            n = validar(0)
            v = cargar_equipos(n)

        elif op == 2:
            if v:
                r1 = cargar_en_rango(1, 6, "Ingrese un rango: ")
                mostrar_equipos(v, r1)

            else:
                print("el vector no fue cargado todavía...")

        elif op == 3:
            if v:
                mat = contar_equipos(v)
                mostrar_matriz(mat)

            else:
                print("El vector no fue cargado todavía...")

        elif op == 4:
            if v:
                generar_archivo(fd, v, 600)
            else:
                print("El vector no fue cargado todavía...")

        elif op == 5:
            if os.path.exists(fd):
                mostrar_archivo(fd)
            else:
                print("El archivo", fd, "no existe...")

        elif op == 6:
            print()
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == "__main__":
    main()
