class Ttp:
    #TtP : Treatment to people
    def __init__(self,Dni,name,surname,diagnostic,dinero,complejidad):
        self.Dni = Dni
        self.name = str(name)
        self.surname = str(surname)
        self.diagnostic = diagnostic
        self.dinero = dinero
        self.complejidad = complejidad

    def __str__(self):
        r = "Dni:{} ,name:{}, surname:{}, diagnostic:{}, dinero:{}, complejidad:{}"
        return r.format(self.Dni,self.name,self.surname,self.diagnostic,self.dinero,self.complejidad)



if __name__ == '__main__':
    p = Ttp(47909207,"Leandro","Rios Bas","Feliz","999999999999","Soy_Dios")
    print(p)