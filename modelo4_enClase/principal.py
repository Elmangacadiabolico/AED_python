import os.path
import pickle
import random

from clase import Seguro


# Muestra las opciones, y carga y retorna la que elija el usuario.
def menu():
    print("1. Cargar (con inserción ordenada)")
    print("2. Mostrar (de acuerdo a lo requerido)")
    print("3. Búsqueda y descuento (según sea requerido)")
    print("4. Generar archivo binario (de acuerdo a lo requerido)")
    print("5. Mostrar archivo binario (de acuerdo a lo requerido)")
    print("6. Salir del programa.")
    return int(input("Ingrese la opción: "))


# Genera con datos aleatorios un objeto de la clase Seguro y lo retorna.
def generar_aleatorio():
    NOMBRES = (
        "Agustina", "Bruno", "Camila", "Diego", "Elena", "Facundo", "Gabriela",
        "Hernán", "Irene", "Joaquín", "Karina", "Lucas", "Mariana", "Nicolás",
        "Olivia", "Pablo", "Quimey", "Ramiro", "Sofía", "Tomás", "Valentina",
        "Walter", "Ximena", "Yamila", "Zoe"
    )
    APELLIDOS = (
        "Acosta", "Benítez", "Castro", "Domínguez", "Escobar", "Flores",
        "Gómez", "Herrera", "Ibáñez", "Juárez", "Luna", "Molina", "Núñez",
        "Ortiz", "Peralta", "Quiroga", "Ramírez", "Sosa", "Torres", "Vega"
    )

    codigo = random.randint(1, 99_999)
    nombre = random.choice(NOMBRES) + " " + random.choice(APELLIDOS)
    tipo = random.randint(1, 5)
    propietario = random.choice((True, False))
    monto = round(random.uniform(8_000, 95_000), 2)
    return Seguro(codigo, nombre, tipo, propietario, monto)


# Carga y retorna un número, validando que sea mayor al valor inf que entra como parámetro.
def validar(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio mayor a ' + str(inf) + '... Cargue de nuevo: '))
    return n


# Función principal o de arranque.
def main():
    random.seed(13715)
    fd = "archivo.dat"
    v = []
    op = -1
    while op != 6:
        op = menu()
        if op == 1:
            pass

        elif op == 2:
            if v:
                pass
            else:
                print("El vector no fue cargado todavía...")

        elif op == 3:
            if v:
                pass
            else:
                print("El vector no fue cargado todavía...")

        elif op == 4:
            if v:
                pass
            else:
                print("El vector no fue cargado todavía...")

        elif op == 5:
            pass

        elif op == 6:
            print()
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == "__main__":
    main()
