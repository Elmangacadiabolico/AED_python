from clase import *
import os.path
import pickle
def ordenar_titulo():
    pass
def csv_to_serie(i):
    pass
def generar_archivo(v,idioma,fd):
    f = open(fd, 'wb')
    for i in v:
        if i.idioma == idioma and i.temporadas >1:
            pickle.dum(i,f)
    f.close()
def validar_entre():
    pass

def main():
    v = leer_archivo()
    l = ordenar_titulo(v)

    x = -3
    while x != 0:
        print('1.listado de contenido')
        print('2.ingresar idioma')
        print('3.Buscar')
        print('4.determinar duracion')
        print('5.listado de contenido')

        if x == 1:
            pass

        if x == 2:
            idioma= validar_entre()
            df = 'series' + str(idioma) +'.dat'
            generar_archivo()


def leer_archivo():
    v = list()
    ruta = 'series.csv'
    if not os.path.exists(ruta):
        return print('archivo no encontrado y/o No existente')
    m = open(ruta,'rt')
    for i in m:
        if primer_linea:
            primer_linea = False
            continue
        serie = csv_to_serie(i)
        v.append(serie)
    m.close()
    print('ando')
    return v

if __name__ == '__main__':
    main()