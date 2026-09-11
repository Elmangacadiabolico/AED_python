def read(leg, nom, pro):
    n = len(leg)
    for i in range(n):
        leg[i] = int(input('Legajo: '))
        nom[i] = input('Nombre: ')
        pro[i] = float(input('Promedio: '))


def procesar(leg, nom, pro):
    im = 0
    for i in range(1,len(pro)):
        if pro[i] > pro[im]:
            im = i
    return leg[im], nom[im], pro[im]


def test():
    n = int(input('Cantidad de alumnos: '))
    leg = n * [0]
    nom = n * ['']
    pro = n * [0.0]
    read(leg, nom, pro)

    r = procesar(leg, nom, pro)

    print('Datos del estudiante pedido...')
    print('Legajo:', r[0])
    print('Nombre:', r[1])
    print('Promedio:', r[2])


if __name__ == '__main__':
    test()