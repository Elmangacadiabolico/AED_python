import random
import os.path
from Clases import *
import pickle



def main():
    menu()
    pass
def menu():
    v = []
    x = -3
    while x != 0:
        print('1\tCarga')
        print('2\tMostrar')
        print('3\tBuscar')
        print('4\tCrear')
        print('5\tLeer')
        print('0\tCarga')
        x = int(input('Ingrese una opcion:'))
        if x == 1 and not v:
            v=Cargar(v)
        if v:
            if x == 2:
                Mostrar(v)
            if x == 3:
                resultado_busqueda(v)

            if x == 4:
                Writen(v)
            if x == 5:
                Read(v)
            if x == 0:
                print('Programa Finalizado')
def validar():
    inf = int(input('Ingrese un numero:'))
    while not  inf > 0 :
        inf = int(input('Ingrese un numero entero positivo mayor a 0:'))
    return inf
def Cargar(v):
    x = validar()
    NOMBRES = [
        'Sabina', 'Alejo', 'Pepe', 'Jesús', 'Shadi', 'Carlos', 'Ana', 'José', 'María', 'Pedro','Belén', 'Martín', 'Soledad', 'Lucía', 'Mateo', 'Valentina', 'Santiago', 'Camila', 'Facundo', 'Florencia','Nicolás', 'Julieta', 'Joaquín', 'Agustina', 'Tomás', 'Milagros', 'Lautaro', 'Candela', 'Franco', 'Rocío','Bruno', 'Antonella', 'Gonzalo', 'Micaela', 'Ezequiel', 'Daniela', 'Matías', 'Paula', 'Federico', 'Carolina',
        'Sebastián', 'Natalia', 'Rodrigo', 'Romina', 'Maximiliano', 'Verónica', 'Leandro', 'Gabriela', 'Emiliano','Laura','Ignacio', 'Mariana', 'Damián', 'Silvana', 'Hernán', 'Cecilia', 'Diego', 'Patricia', 'Andrés', 'Marcela','Gustavo', 'Alejandra', 'Fernando', 'Sofía', 'Javier', 'Elena', 'Ricardo', 'Clara', 'Pablo', 'Inés',
        'Luciano', 'Renata', 'Esteban', 'Victoria', 'Marcos', 'Abril', 'Ramiro', 'Jazmín', 'Alan', 'Brenda','Julián', 'Ludmila', 'Cristian', 'Noelia', 'Axel', 'Pilar', 'Iván', 'Ailén', 'Gael', 'Delfina','Thiago', 'Morena', 'Benjamín', 'Emma', 'Santino', 'Olivia', 'Bautista', 'Mía', 'Lionel', 'Guadalupe',
    ]
    for i in range(x):
        ide = random.randint(1,900)
        Nombre = random.choice(NOMBRES)
        cliente = random.choice(NOMBRES)
        lenguaje = random.randint(1,5)
        horas = random.randint(0,3000)
        proyectos = Proyecto(ide,Nombre,cliente,lenguaje,horas)
        add_in_orden(proyectos,v)
    return v
def add_in_orden(proyectos,v):
    isq,der = 0,len(v)-1
    pos = len(v)

    while isq <= der:
        c = (isq+der)//2
        if proyectos.ide == v[c].ide:
            pos = c
        if proyectos.ide > v[c].ide:
            isq = c +1
        else:
            der = c-1
    if isq > der:
        pos = isq
    v[pos:pos] =[proyectos]
def Mostrar(v):
    for i in range(len(v)):
        print(v[i])
def resultado_busqueda(v):
    x = validar()
    pos = Buscar_num(v,x)
    if pos == -1:
        print('No se encontro el valor buscado')
        return None
    print('valor encontrado',v[pos])
    if v[pos].lenguaje == 'JavaScript':
        v[pos].horas += (v[pos].horas*8)//100
        print('modificado',v[pos])
def Buscar_num(v,x):

    isq,der = 0,len(v)-1

    while isq <= der:
        c = (isq+der)//2
        if x == v[c].ide:
            print('se encontro el valor buscado',x)
            return c
        if x > v[c].ide:
            isq = c +1
        else:
            der = c-1

    return -1
def Writen(v):
    n = len(v)
    texto = 'Proyectos'
    m = open(texto, 'wb')
    y = promedio(v)
    for i in range(n):
        if v[i].horas > y:
            pickle.dump(v[i],m)
    m.close()
def promedio(v):
    cc = 0
    c = 0
    for i in range(len(v)):
        c += 1
        cc += v[i].horas
    porm = (c//cc)
    return porm
def Read(v):
    texto = 'Proyectos'
    if not os.path.exists(texto):
        print('no Existe el archivo')
        return
    m = open(texto, 'rb')
    t = os.path.getsize(texto)
    while m.tell() < t:
        print(pickle.load(m))
    m.close()


if __name__ =='__main__':
    main()