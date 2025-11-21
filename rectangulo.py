# Importamos la clase base FiguraGeometrica
from figura_geometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    # Constructor que recibe ancho y alto
    def __init__(self, ancho: float, alto: float):
        # Llamamos al constructor de la clase base
        super().__init__(ancho, alto)

    # Sobrescribimos área para usar la fórmula del rectángulo
    def area(self)-> float:
        return self.ancho * self.alto

    # Sobrescribimos perimetro para la fórmula del rectángulo
    def perimetro(self)-> float:
        return 2 * (self.ancho + self.alto)

    # Sobrescribimos __str__ para mostrar las dimensiones
    def __str__(self)-> str:
        return f"Rectangulo(ancho={self.ancho}, alto={self.alto})"
