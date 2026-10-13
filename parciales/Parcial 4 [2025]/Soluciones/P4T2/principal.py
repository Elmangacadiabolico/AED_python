import os.path
import pickle
import random

# Use la forma de importación que prefiera.
# Comente una y descomente la otra, a su gusto.
# import clase
from clase import Mago


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
        "Albus Dumbledore", "Lord Voldemort", "Nymphadora Tonks", "Severus Snape", "Sirius Black",
        "Harry Potter", "Hermione Granger", "Ron Weasly", "Ginny Weasly", "Luna Lovegood",
        "Alastor Moody", "Bellatrix Lestrange", "Remus Lupin", "Minerva McGonagall", "Lucius Malfoy",
        "Arthur Weasley", "Fleur Delacour", "Viktor Krum", "Draco Malfoy", "Neville Longbottom",
        "Hagrid", "Lily Potter", "Amelia Bones", "James Potter ", "Narcissa Malfoy", "Molly Weasley",
        "Peter Pettigrew ", "Aberforth Dumbledore", "Garrick Ollivander", "Madame Maxime", "Rodolphus Lestrange",
        "Augustus Rookwood", "Cornelius Fudge", "Dolores Umbridge", "Charlie Weasley", "Xenophilius Lovegood",
        "Sybill Trelawney", "Andromeda Tonks", "Cho Chang", "Seamus Finnigan", "Parvati Patil",
        "Gellert Grindelwald", "Filius Flitwick", "Kingsley Shacklebolt", "Godric Gryffindor",
        "Antonin Dolohov", "Salazar Slytherin", "Rowena Ravenclaw", "Helga Hufflepuff", "Horace Slughorn"
    )

    nombre = random.choice(NOMBRES)
    casa = random.randint(1, 4)
    nivel = random.randint(1, 10)
    hechizos = random.randint(1, 1000)
    puntaje = random.randint(1, 100)
    return Mago(nombre, casa, nivel, hechizos, puntaje)


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
                print("el vector no fue cargado todavía...")

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
            if os.path.exists(fd):
                pass
            else:
                print("El archivo", fd, "no existe...")

        elif op == 6:

            print()
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == "__main__":
    main()
