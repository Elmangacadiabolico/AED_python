class Proyecto:
    def __init__(self,ide,nombre,cliente,lenguaje,horas):
        self.ide = int(ide)
        self.nombre = str(nombre)
        self.cliente = str(cliente)
        Codex = ['Python','Java','TypeScript','JavaScript','Go']
        self.lenguaje = Codex[lenguaje -1]
        self.horas = int(horas)

    def __str__(self):
        r = 'Ide:{},Nombre:{},Cliente:{},Lenguaje De Programa:{},Horas:{}hs'
        return r.format(self.ide,self.nombre,self.cliente,self.lenguaje,self.horas)
