def crear_matriz(v):
    m = 5   #m = columna  #idioma
    n = 6  #n = fila  #genero

    matriz = [[0]*m for i in range(n)]

    conteo = [0] * 6
    for i in range(len(v)):
        fila = v[i].idioma #
        columna = v[i].genero #
        #conteo[indice] += 1
        matriz[fila][columna] += 1
    return matriz

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] >0:
                print('para el genero',i,'y el idioma',j,'hay',matriz[i][j],'series')


##la funcion de crear matriz es un punto

if __name__ == '__main__':
    matriz =crear_matriz(v)
    mostrar_matriz(matriz)
