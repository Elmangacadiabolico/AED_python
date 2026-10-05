class Tratamiento:

    def __init__(self, dni, nombre, apellido, diagnostico, monto_base, complejidad, algoritmo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.diagnostico = diagnostico
        self.monto_base = monto_base
        self.complejidad = complejidad
        self.algoritmo = algoritmo
        self.monto_final = 0

    def __str__(self):
        r = "DNI: {} - Nombre: {} - Apellido: {} - Diagnostico: {} - Monto base: {} - Complejidad: {} - Algoritmo: {} - Monto final: {}"
        return r.format(self.dni, self.nombre, self.apellido, self.diagnostico,
                        self.monto_base, self.complejidad, self.algoritmo, self.monto_final)

def procesar_linea(linea):
    partes = linea.split(",")
    Dni = int(partes[0])
    name = partes[1]
    surname = partes[2]
    diagnostic = partes[3]
    monto_base = float(partes[4])
    complejidad = partes[5]
    ide  = partes[6]
    t = Tratamiento(Dni, name, surname, diagnostic, monto_base, complejidad,ide)

    return t