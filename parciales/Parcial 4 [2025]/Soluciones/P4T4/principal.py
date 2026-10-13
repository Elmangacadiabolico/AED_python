import os.path
import pickle
import random

# Use la forma de importación que prefiera.
# Comente una y descomente la otra, a su gusto.
# import clase
from clase import Puesto


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
        "La Parrilla del Gordo", "BurgerManía", "Cheddar House", "La Cordobesa", "Punto Grill",
        "Smoky’s BBQ", "Guerrilla Burger", "El Patio", "Burger Lab", "La Esquina de la Carne",
        "Big Toro", "Crispy Town", "Chori&Burgers", "Don Angus", "Urban Bites", "El Fogón Moderno",
        "Mundo Burger", "Black Angus", "La Tentación", "Criolla Smash", "Sabores del Cerro",
        "Güemes Grill", "El Hambre Feliz", "Barrio Burger", "Burger del Centro"
    )

    nombre = random.choice(NOMBRES)
    barrio = random.randint(1, 12)
    tipo = random.randint(1, 6)
    puntaje = random.randint(100, 500)
    return Puesto(nombre, barrio, tipo, puntaje)


def cargar_en_rango(lim_inf, lim_sup, mensaje='Ingrese un valor'):
    n = int(input(mensaje))
    while n < lim_inf or n > lim_sup:
        n = int(input(f'Error. Se espera un valor entre {lim_inf} y {lim_sup}. {mensaje}'))
    return n


# Función principal o de arranque.
def add_in_order(v, puesto):
    n = pos = len(v)
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2
        if puesto.puntaje == v[c].puntaje:
            pos = c
            break

        if puesto.puntaje > v[c].puntaje:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [puesto]


def cargar_puestos(n):
    v = []
    for i in range(n):
        c = generar_aleatorio()
        add_in_order(v, c)
    return v


def mostrar_puestos(v):
    for p in v:
        print(p)

    for i in range(3):
        print(v[i].nombre)


def buscar_por_puntaje(v, puntaje):
    n = len(v)
    pos = -1
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2
        if puntaje == v[c].puntaje:
            pos = c
            break

        if puntaje > v[c].puntaje:
            der = c - 1
        else:
            izq = c + 1

    return pos


def calcular_porcentaje(muestra, total):
    porcentaje = 0
    if total > 0:
        porcentaje = muestra * 100 / total
    return porcentaje


def calcular_promedio(acum, cont):
    prom = 0
    if cont > 0:
        prom = acum / cont
    return prom


def calcular_promedio_puntaje(v):
    acum = cont = prom = 0
    for p in v:
        acum += p.puntaje
        cont += 1

    return calcular_promedio(acum, cont)


def generar_archivo(fd, v, promedio):
    m = open(fd, 'wb')

    for p in v:
        if p.puntaje >= promedio:
            pickle.dump(p, m)
    m.close()


def mostrar_archivo(fd, barrio):
    cont_barrio = cont = 0
    tam = os.path.getsize(fd)
    m = open(fd, 'rb')

    while m.tell() < tam:
        p = pickle.load(m)
        print(p)
        if p.barrio == barrio:
            cont_barrio += 1
        cont += 1

    m.close()
    promedio = calcular_porcentaje(cont_barrio, cont)
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
            v = cargar_puestos(n)

        elif op == 2:
            if v:
                mostrar_puestos(v)

            else:
                print("el vector no fue cargado todavía...")

        elif op == 3:
            if v:
                puntaje = validar(0)
                pos = buscar_por_puntaje(v, puntaje)
                if pos != -1:
                    puesto = v[pos]
                    print(puesto)
                    if puesto.puntaje >= 250:
                        puesto.puntaje *= 1.09
                        print(puesto)
                else:
                    print("¡Puesto inexistente!")

            else:
                print("El vector no fue cargado todavía...")

        elif op == 4:
            if v:
                promedio = calcular_promedio_puntaje(v)
                generar_archivo(fd, v, promedio)
            else:
                print("El vector no fue cargado todavía...")

        elif op == 5:
            if os.path.exists(fd):
                barrio = cargar_en_rango(1, 12)
                mostrar_archivo(fd, barrio)
            else:
                print("El archivo", fd, "no existe...")

        elif op == 6:
            print()
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == "__main__":
    main()
