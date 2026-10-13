class Mago:
    def __init__(self, nombre, casa, nivel_magico, hechizos, puntaje):
        self.nombre = nombre
        self.casa = casa
        self.nivel_magico = nivel_magico
        self.hechizos = hechizos
        self.puntaje = puntaje

    def __str__(self):
        return f"{self.nombre:<20} - Casa {self.casa:>1} - Nivel {self.nivel_magico:>2}" \
               f" - Hechizos: {self.hechizos:>4} - Puntaje: {self.puntaje:>3}"
