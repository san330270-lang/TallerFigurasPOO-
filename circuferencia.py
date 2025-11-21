from figura_geometrica import FiguraGeometrica
import math

class Circumference(FiguraGeometrica):
    def __init__(self, radio: float):
        # enviamos el radio como ancho y alto
        # porque la clase base requiere dos valores
        super().__init__(radio, radio)

    @property
    def radio(self):
        return self.ancho

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self._ancho = valor
        self._alto = valor

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Circumference(radio={self.radio})"



