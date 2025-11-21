class FiguraGeometrica:
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    #  ANCHO
    @property
    def ancho(self)-> float:
        return self._ancho

    @ancho.setter
    def ancho(self, valor: float):
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que 0")
        self._ancho = valor

    #  ALTO
    @property
    def alto(self)-> float:
        return self._alto

    @alto.setter
    def alto(self, valor: float):
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que 0")
        self._alto = valor

    #  MÉTODOS
    def area(self):
        return self.ancho * self.alto

    def perimetro(self)-> float:
        raise NotImplementedError("Este método debe ser sobrescrito")

    def __str__(self)-> str:
        return f"FiguraGeometrica(ancho={self.ancho}, alto={self.alto})"
