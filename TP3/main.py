from modulo_objet import *
import os.path

def OP1():
    tratamientos = []
    c = 0
    archivo = 'tratamientos.csv'
    if not os.path.exists(archivo):
        return print('Archivo inexistente!')
    m = open(archivo,'rt')
    m.readline()
    for linea in m:
        if linea[-1] == '\n':
            linea = linea[:-1]
        t = procesar_linea(linea)
        tratamientos.append(t)
        c += 1
    m.close()


    return tratamientos


def procesar_linea(linea):
    partes = linea.split(",")
    print(partes)
    for i in range(10):
        Dni = int(partes[0])
        name = partes[1]
        surname = partes[2]
        Dignostic = partes[3]
        monto = float(partes[4])
        complejidad = partes[5]
        t = Tratamientp(Dni, name, surname, Dignostic,monto, complejidad)
        return t

def r1_2(tratamientos):
    alta_com = 0
    for i in range(len(tratamientos)):
        if tratamientos[i].complejidad == 'A':
            alta_com += 1
        if alta_com == 5:
            return tratamientos[i].surname
    return None


def OP2(tratamientos):
    for i in range(len(tratamientos)):
        print(tratamientos[i])

def main():
    x = -3
    while x != 3:
        print("1. cargar tratamientos")
        print("2. mostrar tratamientos")
        print("3. exit")
        x = int(input('seleccione una opcion: '))

        if x == 1:
            tratamientos = OP1()
            #1.1
            print("r1.1:", len(tratamientos))
            #1.2
            rr1_2 = r1_2(tratamientos)
            if rr1_2 is not None:
                print("r1.2:", rr1_2)
            else:
                print("r1.2: No hay suficientes tratamientos de alta complejidad.")
        elif x == 2:
            OP2(tratamientos)
        elif x == 3:
            print("Fin del programa")


if __name__ == '__main__':
    main()