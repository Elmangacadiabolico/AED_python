class Seguro:
    def __init__(self, codigo, nombre, tipo, propietario, monto):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.propietario = propietario
        self.monto = monto

    def __str__(self):
        condicion = "Propietario" if self.propietario else "No propietario"
        return (f"Cód: {self.codigo:>5} - {self.nombre:<25} - Vivienda tipo {self.tipo:>1} - "
                f"{condicion:<14} - Monto mensual: ${self.monto:>10.2f}")
