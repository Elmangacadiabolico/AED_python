


def cargar_tratamientos():
    tratamientos = []
    nombre_archivo = "tratamientos.csv"

    if not os.path.exists(nombre_archivo):
        print("Archivo inexistente!")
        return tratamientos

    archivo = open(nombre_archivo, "rt")
    archivo.readline()  # Ignorar los nombres de las columnas.

    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            tratamiento = procesar_linea(linea)
            tratamientos.append(tratamiento)

    archivo.close()
    return tratamientos


def buscar_quinta_alta(tratamientos):
    cantidad = 0

    for i in range(len(tratamientos)):
        if tratamientos[i].complejidad == "A":
            cantidad = cantidad + 1
            if cantidad == 5:
                return tratamientos[i].apellido

    return None


def opcion_1():
    tratamientos = cargar_tratamientos()
    print("r1.1:", len(tratamientos))

    apellido = buscar_quinta_alta(tratamientos)
    if apellido is None:
        print("r1.2: No hay suficientes tratamientos de alta complejidad.")
    else:
        print("r1.2:", apellido)

    return tratamientos


def obtener_numero(diagnostico):
    posicion_punto = diagnostico.index(".")
    numero = int(diagnostico[posicion_punto + 1:])
    return numero


def obtener_bloque(diagnostico):
    posicion_punto = diagnostico.index(".")
    bloque = int(diagnostico[1:posicion_punto])
    return bloque


def calcular_porcentaje_normal(tratamiento):
    # Esta es la fórmula normal que venían usando.
    numero = obtener_numero(tratamiento.diagnostico)
    porcentaje = tratamiento.monto_base * numero / 100
    return porcentaje


def calcular_monto_algoritmo_1(tratamiento):
    monto_extra = 0
    suma_fija = 0

    if tratamiento.monto_base <= 60000:
        monto_extra = 0
    if tratamiento.monto_base > 60000:
        monto_extra = calcular_porcentaje_normal(tratamiento)

        letra = tratamiento.diagnostico[0]
        if tratamiento.complejidad == "A" and letra != "U":
            suma_fija = tratamiento.monto_base / 2

    monto_final = tratamiento.monto_base + monto_extra + suma_fija
    return monto_final


def calcular_monto_algoritmo_2(tratamiento):
    letra = tratamiento.diagnostico[0]

    if "A" <= letra <= "P":
        monto_extra = calcular_porcentaje_normal(tratamiento)

    elif tratamiento.complejidad == "A":
        numero = obtener_numero(tratamiento.diagnostico)
        porcentaje = numero * 2
        monto_extra = tratamiento.monto_base * porcentaje / 100

    else:
        monto_extra = tratamiento.monto_base * 15 / 100

    monto_final = tratamiento.monto_base + monto_extra
    return monto_final


def calcular_monto_algoritmo_3(tratamiento):
    letra = tratamiento.diagnostico[0]
    monto_extra = 0

    if tratamiento.complejidad == "A":
        monto_extra = tratamiento.monto_base * 30 / 100

    if "A" <= letra <= "L":
        monto_extra = monto_extra + 20000
    elif "M" <= letra <= "P":
        bloque = obtener_bloque(tratamiento.diagnostico)
        monto_extra = monto_extra + 15000 + 5000 * bloque
    else:
        monto_extra = monto_extra + tratamiento.monto_base * 10 / 100

    if monto_extra > 60000:
        monto_extra = 60000

    monto_final = tratamiento.monto_base + monto_extra
    return monto_final


def calcular_monto_algoritmo_4(tratamiento):
    letra = tratamiento.diagnostico[0]
    monto_extra = 0

    if letra == "C":
        if tratamiento.complejidad == "A":
            monto_extra = tratamiento.monto_base * 50 / 100
        else:
            monto_extra = tratamiento.monto_base * 25 / 100

        # El tope de 15.000 solo se aplica para la letra C.
        if monto_extra > 15000:
            monto_extra = 15000

    elif letra == "A" or letra == "B":
        monto_extra = 12000

    else:
        monto_extra = tratamiento.monto_base * 8 / 100

    monto_final = tratamiento.monto_base + monto_extra
    return monto_final


def calcular_monto_normal(tratamiento):
    # Para algoritmos distintos de 1, 2, 3 y 4 se usa el cálculo normal.
    monto_extra = calcular_porcentaje_normal(tratamiento)
    monto_final = tratamiento.monto_base + monto_extra
    return monto_final


def calcular_monto(tratamiento):
    if tratamiento.algoritmo == 1:
        return calcular_monto_algoritmo_1(tratamiento)
    elif tratamiento.algoritmo == 2:
        return calcular_monto_algoritmo_2(tratamiento)
    elif tratamiento.algoritmo == 3:
        return calcular_monto_algoritmo_3(tratamiento)
    elif tratamiento.algoritmo == 4:
        return calcular_monto_algoritmo_4(tratamiento)
    else:
        return calcular_monto_normal(tratamiento)


def calcular_montos_finales(tratamientos):
    for i in range(len(tratamientos)):
        tratamientos[i].monto_final = calcular_monto(tratamientos[i])


def calcular_diferencia_promedio(tratamientos):
    suma_diferencias = 0

    for i in range(len(tratamientos)):
        diferencia = (
            tratamientos[i].monto_final - tratamientos[i].monto_base
        )
        suma_diferencias = suma_diferencias + diferencia

    promedio = suma_diferencias / len(tratamientos)
    return promedio


def contar_diagnosticos_por_letra(tratamientos):
    cantidades = [0] * 26

    for i in range(len(tratamientos)):
        letra = tratamientos[i].diagnostico[0]
        posicion = ord(letra) - ord("A")
        cantidades[posicion] = cantidades[posicion] + 1

    return cantidades


def buscar_letra_mas_frecuente(cantidades):
    posicion_mayor = 0

    for i in range(1, len(cantidades)):
        if cantidades[i] > cantidades[posicion_mayor]:
            posicion_mayor = i

    letra = chr(posicion_mayor + ord("A"))
    cantidad = cantidades[posicion_mayor]
    return letra, cantidad


def buscar_dni_mayor_monto_alta(tratamientos):
    mayor = None

    for i in range(len(tratamientos)):
        tratamiento = tratamientos[i]

        if tratamiento.complejidad == "A":
            if mayor is None:
                mayor = tratamiento
            elif tratamiento.monto_final > mayor.monto_final:
                mayor = tratamiento

    if mayor is None:
        return None

    return mayor.dni


def opcion_2(tratamientos):
    if len(tratamientos) == 0:
        print("No hay tratamientos cargados.")
        return

    calcular_montos_finales(tratamientos)

    promedio = calcular_diferencia_promedio(tratamientos)
    print("r2.1:", round(promedio, 2))

    cantidades = contar_diagnosticos_por_letra(tratamientos)
    letra, cantidad = buscar_letra_mas_frecuente(cantidades)
    print("r2.2:", letra)
    print("r2.3:", cantidad)

    dni = buscar_dni_mayor_monto_alta(tratamientos)
    if dni is None:
        print("r2.4: No hay tratamientos de alta complejidad.")
    else:
        print("r2.4:", dni)


def mostrar_menu():
    print("1. Cargar tratamientos")
    print("2. Mostrar resultados")
    print("0. Salir")


def main():
    tratamientos = []
    opcion = -1

    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Ingrese opción: "))

        if opcion == 1:
            tratamientos = opcion_1()
        elif opcion == 2:
            opcion_2(tratamientos)


if __name__ == "__main__":
    main()