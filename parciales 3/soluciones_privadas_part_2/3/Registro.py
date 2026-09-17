class taxi:
    def __init__(self,ide,DNI,modelo,tarifa):
        self.ide = ide
        self.DNI = DNI
        self.modelo = modelo
        self.tarifa = tarifa
    def __str__(self):
        r = 'numero de serie:{},Dni:{},marca:{},tarifa:{}$por km'
        return r.format(self.ide,self.DNI,self.modelo,self.tarifa)

if __name__ == '__main__':
    p = taxi(30,10,3,1000)
    print(p)