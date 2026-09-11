def calcular_producto_digitos(numero):
    producto = 1
    temp = numero
    while temp > 0:
        digito = temp % 10
        producto = producto * digito
        temp = temp // 10
    return producto



def procesar_numero(numero):
    pasos = 0
    aux = numero
    secuencia = "(" + str(numero)

    while aux >= 10:
        aux = calcular_producto_digitos(aux)
        pasos = pasos + 1
        secuencia = secuencia + ", " + str(aux)

    secuencia = secuencia + ")"
    return pasos, secuencia



def buscar_mayor_persistencia(lim_izq, lim_der):
    mas_pasos = 0
    nmp = 0
    secuencia_mayor = ""

    for n in range(lim_izq, lim_der + 1):
        pasos, secuencia = procesar_numero(n)

        if pasos > mas_pasos:
            mas_pasos = pasos
            nmp=n
            secuencia_mayor = secuencia

    return nmp, mas_pasos, secuencia_mayor



n, p, s = buscar_mayor_persistencia(4000, 7000)

print("Número con mayor persistencia:", n)
print("Persistencia:", p)
print("Secuencia:", s)