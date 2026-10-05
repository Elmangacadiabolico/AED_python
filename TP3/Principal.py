from modulo_objet import *

def procesar_linea(linea):
    partes = linea.split(",")
    dni = int(partes[0])
    nombre = partes[1]
    apellido = partes[2]
    diagnostico = partes[3]
    monto_base = float(partes[4])
    complejidad = partes[5]
    algoritmo = int(partes[6])
    return Tratamiento(dni, nombre, apellido, diagnostico, monto_base, complejidad, algoritmo)


def cargar_tratamientos():
    tratamientos = []
    archivo = open("tratamientos.csv", "rt")
    archivo.readline()  # se ignora la línea de encabezado
    for linea in archivo:
        linea = linea.strip()  # elimina \n y \r
        if linea != "":
            tratamientos.append(procesar_linea(linea))
    archivo.close()
    return tratamientos


def buscar_quinta_alta(tratamientos):
    cantidad = 0
    for i in range(len(tratamientos)):
        if tratamientos[i].complejidad == "A":
            cantidad += 1
            if cantidad == 5:
                return tratamientos[i].apellido
    return None


def opcion_1():
    tratamientos = cargar_tratamientos()
    print("r1.1:", len(tratamientos))
    apellido = buscar_quinta_alta(tratamientos)
    if apellido is not None:
        print("r1.2:", apellido)
    else:
        print("r1.2: No hay suficientes tratamientos de alta complejidad.")
    return tratamientos


def obtener_numero(diagnostico):
    pos = diagnostico.index(".")
    return int(diagnostico[pos + 1:])


def obtener_bloque(diagnostico):
    pos = diagnostico.index(".")
    return int(diagnostico[1:pos])


def porcentaje_normal(t):
    return t.monto_base * obtener_numero(t.diagnostico) / 100


def monto_algoritmo_1(t):
    porcentaje_extra = 0
    suma_fija = 0
    if t.monto_base > 60000:
        porcentaje_extra = porcentaje_normal(t)
        if t.complejidad == "A" and t.diagnostico[0] != "U":
            suma_fija = t.monto_base / 2
    return t.monto_base + porcentaje_extra + suma_fija


def monto_algoritmo_2(t):
    letra = t.diagnostico[0]
    if "A" <= letra <= "P":
        porcentaje_extra = porcentaje_normal(t)
    elif t.complejidad == "A":
        porcentaje_extra = t.monto_base * (obtener_numero(t.diagnostico) * 2) / 100
    else:
        porcentaje_extra = t.monto_base * 15 / 100
    return t.monto_base + porcentaje_extra


def monto_algoritmo_3(t):
    letra = t.diagnostico[0]
    monto_extra = 0
    if t.complejidad == "A":
        monto_extra = t.monto_base * 30 / 100

    if "A" <= letra <= "L":
        monto_extra += 20000
    elif "M" <= letra <= "P":
        monto_extra += 15000 + 5000 * obtener_bloque(t.diagnostico)
    else:
        monto_extra += t.monto_base * 10 / 100

    if monto_extra > 60000:
        monto_extra = 60000
    return t.monto_base + monto_extra

def recargo_alta_complejidad(t, monto):
    """Recargo del 5% (seguro de vida) del TP2 para tratamientos de alta complejidad."""
    if t.complejidad == "A":
        return monto * 1.05
    return monto

def monto_normal(t):
    """Cálculo normal (algoritmos no listados en la tabla)."""
    monto = t.monto_base + porcentaje_normal(t)
    # ------------------------------------------------------------------
    # DUDA PENDIENTE (consultar a la cátedra): ¿el cálculo normal incluye
    # el 5% de recargo del TP2 para alta complejidad?
    # Si la respuesta es SÍ: descomentar la línea de abajo.
    # monto = recargo_alta_complejidad(t, monto)
    # ------------------------------------------------------------------
    return monto

def calcular_monto(t):
    if t.algoritmo == 1:
        return monto_algoritmo_1(t)
    elif t.algoritmo == 2:
        return monto_algoritmo_2(t)
    elif t.algoritmo == 3:
        return monto_algoritmo_3(t)
    return t.monto_base + porcentaje_normal(t)
    #return monto_normal(t)


def calcular_montos_finales(tratamientos):
    for i in range(len(tratamientos)):
        tratamientos[i].monto_final = calcular_monto(tratamientos[i])

def diferencia_promedio(tratamientos):
    suma = 0
    for i in range(len(tratamientos)):
        suma += tratamientos[i].monto_final - tratamientos[i].monto_base
    return suma / len(tratamientos)


def contar_por_letra(tratamientos):
    conteo = 26 * [0]
    for i in range(len(tratamientos)):
        indice = ord(tratamientos[i].diagnostico[0]) - ord("A")
        conteo[indice] += 1
    return conteo


def letra_mas_frecuente(conteo):
    pos_mayor = 0
    for i in range(1, len(conteo)):
        if conteo[i] > conteo[pos_mayor]:
            pos_mayor = i
    return chr(pos_mayor + ord("A")), conteo[pos_mayor]


def dni_mayor_monto_alta(tratamientos):
    mayor = None
    for i in range(len(tratamientos)):
        t = tratamientos[i]
        if t.complejidad == "A" and (mayor is None or t.monto_final > mayor.monto_final):
            mayor = t
    if mayor is None:
        return None
    return mayor.dni


def opcion_2(tratamientos):
    calcular_montos_finales(tratamientos)
    print("r2.1:", diferencia_promedio(tratamientos))
    letra, cantidad = letra_mas_frecuente(contar_por_letra(tratamientos))
    print("r2.2:", letra)
    print("r2.3:", cantidad)
    print("r2.4:", dni_mayor_monto_alta(tratamientos))
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
        elif opcion == 2 and len(tratamientos) > 0:
            opcion_2(tratamientos)


if __name__ == "__main__":
    main()
