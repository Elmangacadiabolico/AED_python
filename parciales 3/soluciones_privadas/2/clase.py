class producion_pvc:
    def __init__(self,ide,diametro,uso,gramos,ignifugo):
        self.ide = ide #Numero Entero
        self.diametro = diametro
        self.uso = uso #1 al 20
        self.gramos = gramos
        self.ignifugo = ignifugo #1 al 2

    def __str__(self):
        r = "ide:{} ,diametro:{}pie ,uso:{} ,gramos:{} ,ignifugo:{}"
        return r.format(self.ide,self.diametro,self.uso,self.gramos,self.ignifugo)


if __name__ == '__main__':
    p = producion_pvc(900,30,'Codos de desague',100,1 )
    print(p)


