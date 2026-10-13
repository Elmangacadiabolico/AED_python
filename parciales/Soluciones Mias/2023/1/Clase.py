class Lote:
    def __init__(self,Nombre,apellido,NroManzana,LoteManzana,Orientaion,superficie,monto):
        self.Nombre = str(Nombre)
        self.apellido = str(apellido)
        self.NroManzana = int(NroManzana)
        self.LoteManzana = int(LoteManzana)

        self.Orientaion = Orientaion
        self.superficie = superficie
        self.monto = monto

    def __str__(self):
        r = 'Nombre:{},Apellido:{},NroManzana:{},LoteManzana{},Orientaion:{},Superficie:{}m,Monto:{}$'
        return r.format(self.Nombre,self.apellido,self.NroManzana,self.LoteManzana,self.Orientaion,self.superficie,self.monto)