from modulo_objet import*
def OP1(data):
    #intento cargar los datos y conbinarlo con lo que hay en modulo_objet
    arreglo=[None] * len(data)
    for i in range(len(data)):
        linea = data[i]
        campos = []
        campo = ''
        for caracter in linea:
            if caracter == ',' or caracter == '\n':
                campos.append(campo)
                campo = ''
            else:
                campo += caracter
        dni = (campos[0])
        nombre = campos[1]
        apellido = campos[2]
        diagnostico = campos[3]
        dinero = (campos[4])
        complejidad = campos[5]

        arreglo[i] = Ttp(dni,nombre,apellido,diagnostico,dinero,complejidad)


def OP2():
    pass
def info_tratamientos():
    m = open('tratamientos.csv', 'rt')
    t = m.readlines()
    print(t)
    return t

def main():
    data =info_tratamientos()
    x = -3

    while x != 3:
        print("1. cargar tratamientos")
        print("2. mostrar tratamientos")
        print("3. exit")

        x = int(input('seleccione una opcion: '))

        if x == 1 :
            OP1(data)
        elif x == 2 :
            OP2()
        elif x == 3:
            print("Fin del programa")

if __name__ == '__main__':
    main()