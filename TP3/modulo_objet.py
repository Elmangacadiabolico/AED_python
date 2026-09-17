class Tratamientp:
    # TtP : Treatment to people
    def __init__(self, Dni, name, surname, diagnostic, monto, complejidad):
        self.Dni = Dni
        self.name = str(name)
        self.surname = str(surname)
        self.diagnostic = diagnostic
        self.monto = monto
        self.complejidad = complejidad

    def __str__(self):
        r = "Dni:{} ,name:{}, surname:{}, diagnostic:{}, dinero:{}, complejidad:{}"
        return r.format(self.Dni, self.name, self.surname,self.diagnostic, self.monto, self.complejidad)


def procesar_linea(linea):
    partes = linea.split(",")
    Dni = int(partes[0])
    nom = partes[1]
    apeli = partes[2]
    icd10 = partes[3]
    monto = float(partes[4])
    complejidad = partes[5]

    t = Tratamientp(Dni, nom, apeli, icd10, monto, complejidad)

    return t