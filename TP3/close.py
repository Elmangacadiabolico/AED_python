class Tratamientp:
    #TtP : Treatment to people
    def __init__(self,Dni,name,surname,diagnostic,dinero,complejidad,algorit):
        self.Dni = Dni
        self.name = str(name)
        self.surname = str(surname)
        self.diagnostic = diagnostic
        self.dinero = dinero
        self.complejidad = complejidad
        self.algorit = algorit

    def __str__(self):
        r = "Dni:{} ,name:{}, surname:{}, diagnostic:{}, dinero:{}, complejidad:{}, algorit{}"
        return r.format(self.Dni,self.name,self.surname,self.diagnostic,self.dinero,self.complejidad,self.algorit)


def procesar_linea(linea):
    partes = linea.split
    Dni = int(partes[0])
    nom = partes[1]
    apeli = partes[2]
    icd10 = partes[3]
    monto = float(partes[4])
    compleudad = partes[5]
    alog = int(partes[6])
    t = Tratamientp(Dni,nom,apeli,icd10,monto,compleudad,alog)
    return t



if __name__ == '__main__':
    p = Tratamientp(47909207,"Leandro","Rios Bas","Feliz","999999999999","A",2)
    print(p)