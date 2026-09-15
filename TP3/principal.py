import os.path
from close import *
def principal():
    x = -3
    while x != 0:
        print('1.\tLeer')
        print('2.\tLeer')
        print('3.\tLeer')
        print('4.\tLeer')
        print('0.\texit')

        x = int(input('Ingese opción:'))

        if x == 1:
             tratamientos = read()
        print("r1.1:",tratamientos)
        print('r1.2:',tratamientos[4].apellido)#los que sean de alta complequidad, siento el 5 sin importar la complejidad

def read():
    tratamientos = []
    c = 0
    archivo = 'tratamientos.csv'
    if not os.path.exists(archivo):
        return print('Archivo inexistente!')
    m = open(archivo,'rt')
    m.readline()
    for line in m:
        if line[-1] == '\n':
            line = line[:-1]
        t = procesar_linea(linea)
        tratamientos.append(t)
        c += 1
    m.close()


def procesamiento_linea(linea):
    partes = linea.split(",")
    print(partes)
    for i in range(10):
        Dni = []
        name = []
        surname = []
        Dignostic = []


if __name__ == '__main__':
    principal()