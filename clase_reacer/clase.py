class Tratamientos:
    def __init__(self, dni, nombre, apellido, diagnostico,monto_base, complejidad, algoritmo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.diagnostico = diagnostico
        self.monto_base = monto_base
        self.complejidad = complejidad
        self.algoritmo = algoritmo
        self.monto_final = 0
    def __str__(self):
        texto = "DNI: " + str(self.dni)
        texto = texto + " - Nombre: " + self.nombre
        texto = texto + " - Apellido: " + self.apellido
        texto = texto + " - Diagnóstico: " + self.diagnostico
        texto = texto + " - Monto base: " + str(self.monto_base)
        texto = texto + " - Complejidad: " + self.complejidad
        texto = texto + " - Algoritmo: " + str(self.algoritmo)
        texto = texto + " - Monto final: " + str(self.monto_final)
        return texto


def procesar_linea(linea):
    partes = linea.strip().split(",")

    dni = int(partes[0])
    nombre = partes[1]
    apellido = partes[2]
    diagnostico = partes[3]
    monto_base = float(partes[4])
    complejidad = partes[5]
    algoritmo = int(partes[6])

    tratamiento = Tratamiento(
        dni, nombre, apellido, diagnostico,
        monto_base, complejidad, algoritmo
    )

    return tratamiento


class Cobertura:
    def __init__(self):
        pass
    def __str__(self):
        pass

