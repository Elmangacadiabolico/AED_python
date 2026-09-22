class lista:
    def __init__(self,titulo,genero,idioma,cantidad,duracion):
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma
        self.cantidad=cantidad
        self.duracion=duracion
    def __str__(self):
        r = 'El titulo:{},el genero:{},idioma:{},Cantidad de temporada:{},Su Duracion:{}minutos'
        return r.format(self.titulo,self.genero,self.idioma,self.cantidad,self.duracion)

if __name__ =='__main__':
    p =lista('El pepe','Fantasia',0,3,13)
    print(p)