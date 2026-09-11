class taxis:
    def __init__(self,ide,DNI,marca,tarifa,):
        self.ide = ide
        self.DNI=DNI #
        self.marca = marca #1 al 20
        self.tarifa = tarifa #Km

    def __str__(self):
        r = 'ide:{}\tDNI:{}\tmarca del auto:{}\tTarifa:{}km\t'
        return r.format(self.ide,self.DNI,self.marca,self.tarifa)



if __name__ == '__main__':
    p = taxis(9999,4782,13,130)
    print(p)