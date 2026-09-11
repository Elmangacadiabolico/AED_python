def longitud_primer_sector(t):
    if len(t) == 0 or len(t) == 1:
        return len(t)

    if t[0] == t[1]:
        return 1 + longitud_primer_sector(t[1:])

    return 1


def contar_sectores(t):
    if len(t) == 0 or len(t) == 1:
        return len(t)

    if t[0] != t[1]:
        return 1 + contar_sectores(t[1:])

    return contar_sectores(t[1:])


def mayor_longitud(t):
    if len(t) == 0:
        return 0

    n = longitud_primer_sector(t)
    resto = t[n:]

    mayor_resto = mayor_longitud(resto)

    if n > mayor_resto:
        return n
    else:
        return mayor_resto

def main():
    m = open('copia.txt', 'rt')
    t = m.readline()

    print(longitud_primer_sector(t))
    print(contar_sectores(t))
    print(mayor_longitud(t))

if __name__ == '__main__':
    main()