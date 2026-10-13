class Equipo:
    def __init__(self,ide,Nombre,edad,nivel,Monto):
        self.ide = ide
        self.Nombre = Nombre
        self.edad=edad
        self.nivel=nivel
        self.Monto=Monto

    def __str__(self):
        r = 'Nombre:{},Edad{},Nivel:{},Monto:{}'
        return r.format(self.Nombre,self.edad,self.nivel,self.Monto)




if __name__ == '__main__':
    #p = clase()
    pass