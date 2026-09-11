class Productos:
    def __init__(self,id,caracts,calorias,Tipo,precio):
        self.id = id
        self.caracts = str(caracts)
        self.calorias = calorias
        self.Tipo=Tipo #(1,30)
        self.precion = precio

    def __str__(self):
        r = 'El codigo de productor:{} ,descripcion del producto:{},Calorias del producto:{},tipo de producto{},precio del producto:{}$'
        return r.format(self.id,self.caracts,self.calorias,self.Tipo,self.precion)


if __name__ == '__main__':
    p = Productos(9111,'Contiene carne con mostaza',30,1,0.5)
    print(p)
