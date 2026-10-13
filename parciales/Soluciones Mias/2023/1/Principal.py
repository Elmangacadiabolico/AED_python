from Clase import*
import random
import os.path

def validar():
    inf = int(input('Ingrese un numero:'))
    while not inf > 0:
        inf = int(input('Ingrese un numero mayor que 0: '))
    return inf


def add_in_orden(x,v):
    n = len(v)
    isq,der = 0 , n-1
    pos = n

    while isq <= der:
        c = (isq+der)//2
        if x.Nombre == v[c].Nombre:
            pos = c
            break
        else:
            if x.Nombre<v[c].Nombre:
                der = c-1
            else:
                isq =c+1
    v[pos:pos] = [x]

def Carga_valores():
    x = validar()
    v = []
    Names =['Sabina','Alejo','Pepe','Jesus','Shado','Garden','p',"Carlos", "Ana", "José", "María", "Pedro", "Belén", "Martín", "Soledad"]
    surname = ['pelico','loro','frape','def','Alta','Maria','Jose','isa',"Díaz", "Giuliani", "Trejo", "Masiero", "Duplesis", "Johnson", "Iriarte"]
    for i in range(x):
        Nombre = random.choice(Names)
        Apellidos = random.choice(surname)
        NroManzana = random.randint(1,35)
        LoteManzana = random.randint(1,20)
        Orientaion = random.randint(1,4)
        superficie = round(random.uniform(0,50000),2)
        monto = round(random.uniform(10,50000),2)
        lote = Lote(Nombre,Apellidos,NroManzana,LoteManzana,Orientaion,superficie,monto)
        add_in_orden(lote,v)
    return v



def matriz(v):
    x = validar()
    matriz = [[0] * x for i in range(35)]
    for i in range(len(v)):
        j = v[i].NroManzana -1
        k = v[i].Orientaion -1
        matriz[k][j] += v[i].superficie

    return matriz

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                print('manzana',i + 1,'orientacion',j+1,'superficie',round(matriz[i][j]),2)





def mostrar(v):
    for i in range(len(v)):
        m = v[i].Orientaion
        if m == 1:
            m == 'Norte'
        elif m == 2:
            m == 'Sur'
        elif m == 3:
            m=='Este'
        else:
            if m == 4:
                m == 'Oeste'

        print(v[i])


def main():
    x = -3
    v = []
    while x != 0:
        print('---------Menu----------')
        print('1\tCarga arreglo')
        print('2\tCarga arreglo')
        print('3\tCarga arreglo')
        print('4\tCarga arreglo')
        print('0\tSalir')

        x = int(input('Ingrese un numero:'))
        if x == 1:
            v=Carga_valores()
        if v:
            if x == 2:
                mostrar(v)
            elif x == 3:
                matriz(v)
                mostrar_matriz(matriz)
            elif x == 4:
                pass




if __name__=='__main__':
    main()