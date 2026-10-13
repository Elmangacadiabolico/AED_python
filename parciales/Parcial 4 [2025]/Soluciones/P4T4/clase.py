class Puesto:
    def __init__(self, nombre, barrio, tipo_hamburguesa, puntaje):
        self.nombre = nombre
        self.barrio = barrio
        self.tipo_hamburguesa = tipo_hamburguesa
        self.puntaje = puntaje

    def __str__(self):
        return f"{self.nombre:<22} - Barrio {self.barrio:>2} - Tipo {self.tipo_hamburguesa:>1} " \
               f"- Puntaje Promedio: {self.puntaje:>3}"
