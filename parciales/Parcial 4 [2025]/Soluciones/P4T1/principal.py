import os.path
import pickle
import random

# Use la forma de importación que prefiera.
# Comente una y descomente la otra, a su gusto.
# import clase
from clase import Incursion


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
    NOMBRES = (
        "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon",
        "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie",
        "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill",
        "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate",
        "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu",
        "Sandshrew", "Sandslash", "Nidorino", "Nidorina", "Nidoqueen",
        "Nidorina", "Nidorino", "Nidoking", "Clefairy", "Clefable",
        "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat",
        "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect"
    )

    nombre = random.choice(NOMBRES)
    gimnasio = random.randint(1, 3)
    nivel = random.randint(1, 5)
    tipo = random.randint(1, 3)
    forma = random.randint(1, 2)
    cantidad = random.randint(5, 10)
    adicionales = random.randint(0, 20)
    return Incursion(nombre, gimnasio, nivel, tipo, forma, cantidad, adicionales)


def cargar_en_rango(lim_inf, lim_sup, mensaje='Ingrese un valor'):
    n = int(input(mensaje))
    while n < lim_inf or n > lim_sup:
        n = int(input(f'Error. Se espera un valor entre {lim_inf} y {lim_sup}. {mensaje}'))
    return n


# Función principal o de arranque.
def add_in_order(v, incursion):
    n = pos = len(v)
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2
        if incursion.pokemon == v[c].pokemon:
            pos = c
            break

        if incursion.pokemon < v[c].pokemon:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [incursion]


def cargar_incursiones(n):
    v = []
    for i in range(n):
        c = generar_aleatorio()
        add_in_order(v, c)
    return v


def mostrar_incursiones(v, t):
    acum = cont = 0

    for i in v:
        print(i)
        if i.tipo == t:
            acum += i.nivel
            cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont

    print(f'r.2:{round(prom, 2)}')


def contar_incursiones(v):
    mat = [[0] * 5 for i in range(6)]

    for i in v:
        f = i.jugadores_remotos - 5
        c = i.nivel - 1
        mat[f][c] += 1

    return mat


def mostrar_matriz(m):
    filas, columnas = len(m), len(m[0])

    for f in range(filas):
        for c in range(columnas):
            if m[f][c] > 0:
                print(f'Jugadores {f + 5}, Nivel {c + 1}, Cantidad: {m[f][c]}')


def generar_archivo(fd, v, nivel, tipo):
    m = open(fd, 'wb')

    for i in v:
        if i.nivel == nivel and i.tipo == tipo:
            pickle.dump(i, m)
    m.close()


def mostrar_archivo(fd):
    cont = cont_gym = 0
    tam = os.path.getsize(fd)
    m = open(fd, 'rb')

    while m.tell() < tam:
        i = pickle.load(m)
        print(i)
        if i.gimnasio == 2:
            cont_gym += 1
        cont += 1

    m.close()
    porc = 0
    if cont > 0:
        porc = cont_gym * 100 / cont
    print(f'r5.1: {porc}')


def main():
    random.seed(13715)
    fd = "archivo.dat"
    v = []
    op = -1
    while op != 6:
        op = menu()
        if op == 1:
            n = validar(0)
            v = cargar_incursiones(n)

        elif op == 2:
            if v:
                t = cargar_en_rango(1, 3, "Ingrese un tipo: ")
                mostrar_incursiones(v, t)

            else:
                print("el vector no fue cargado todavía...")

        elif op == 3:
            if v:
                mat = contar_incursiones(v)
                mostrar_matriz(mat)

            else:
                print("El vector no fue cargado todavía...")

        elif op == 4:
            if v:
                generar_archivo(fd, v, 5, 1)
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
