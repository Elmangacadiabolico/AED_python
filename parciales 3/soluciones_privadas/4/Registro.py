class pintura:
    def __init__(self,color,tipo,rendimiento,precio):
        self.color = color
        self.tipo = tipo
        self.rendimiento = rendimiento
        self.precio = precio


    def __str__(self):
        r = 'color:{},tipo de pintura:{},cantidad:{},precio:{}$'
        return r.format(self.color,self.tipo,self.rendimiento,self.precio)


if __name__ =='__main__':
    p = pintura(255,'latex',1000,40)
    print(p)