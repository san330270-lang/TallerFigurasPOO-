# Importamos la clase base FiguraGeometrica
from figura_geometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    # El constructor recibe un solo valor: el lado
    def __init__(self, lado: float):
        # Como un cuadrado tiene ancho y alto iguales, enviamos el mismo valor
        super().__init__(lado, lado)

    # Sobrescribimos el método área para usar la fórmula de un cuadrado
    def area(self)-> float:
        return self.ancho ** 2

    # Sobrescribimos perimetro para la fórmula de un cuadrado
    def perimetro(self)-> float:
        return 4 * self.ancho

    # Sobrescribimos __str__ para mostrar el lado del cuadrado
    def __str__(self)-> str:
        return f"Cuadrado(lado={self.ancho})"

