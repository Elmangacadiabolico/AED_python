class productos_pvc:
    def __init__(self,ide,diametro,tipo,cant,ignifugo):
        self.ide = ide
        self.diametro = int(diametro)
        self.tipo = tipo #1 al 20
        self.cant = cant
        self.ignifugo = ignifugo #2 o 1
    def __str__(self):
        r = 'ide:{}, diametro:{}, tipo:{}, cant:{}, ignifugo:{}'
        return r.format(self.ide,self.diametro,self.tipo,self.cant,self.ignifugo)


if __name__ == '__main__':
    p = productos_pvc(10,30,100,20,1)
    print(p)