class productos:
    def __init__(self,codigos,descripcion,calorias,tipos,precio):
        self.codigos = codigos
        self.descripcion = descripcion
        self.calorias = calorias
        self.tipos = tipos
        self.precio = precio
    def __str__(self):
        r = 'el codigo de producto:{},Descripcion:{},cantidad de calorias:{},tipo:{},precio:{}$'
        return r.format(self.codigos,self.descripcion,self.calorias,self.tipos,self.precio)

if __name__ == '__main__':
    p = productos(1031,1,30,3,0.50)
    print(p)