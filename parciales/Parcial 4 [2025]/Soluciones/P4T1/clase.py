class Incursion:
    def __init__(self, pokemon, gimnasio, nivel, tipo, forma, jugadores_remotos, jugadores_adicionales):
        self.pokemon = pokemon
        self.gimnasio = gimnasio
        self.nivel = nivel
        self.tipo = tipo
        self.forma = forma
        self.jugadores_remotos = jugadores_remotos
        self.jugadores_adicionales = jugadores_adicionales

    def __str__(self):
        return (f"{self.pokemon:<12} | Gimnasio: {self.gimnasio:>1} | Nivel: {self.nivel:>1} | "
                f"Tipo: {self.tipo:>1} | Forma: {self.forma:>1} | "
                f"Remotos: {self.jugadores_remotos:>2} | Adicionales: {self.jugadores_adicionales:>2}")
