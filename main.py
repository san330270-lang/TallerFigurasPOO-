from cuadrado import Cuadrado
from rectangulo import Rectangulo
from circuferencia import Circumference  # <-- nueva figura

# Función que suma las áreas de una lista de figuras
def sumar_areas(figuras: list):
    total = 0
    for f in figuras:
        total += f.area()  # Polimorfismo
    return total

# Función que suma los perímetros de una lista de figuras
def sumar_perimetros(figuras: list):
    total = 0
    for f in figuras:
        total += f.perimetro()
    return total



if __name__ == "__main__":

    print("\n CREACIÓN DE OBJETOS ")

    # Cuadrados
    c1 = Cuadrado(10)
    c2 = Cuadrado(15)

    # Rectángulos
    r1 = Rectangulo(8, 12)
    r2 = Rectangulo(9, 6)

    # Circunferencias
    cir1 = Circumference(6)
    cir2 = Circumference(13)

    # Lista polimórfica
    figuras = [c1, c2, r1, r2, cir1, cir2]

    # Mostrar datos de cada figura
    for f in figuras:
        print(f"{f} → Área: {round(f.area(), 2)} | Perímetro: {round(f.perimetro(), 2)}")

    print("\n SUMA DE ÁREAS Y PERÍMETROS ")
    print("Total áreas:", round(sumar_areas(figuras), 2))
    print("Total perímetros:", round(sumar_perimetros(figuras), 2))

    print("\n PRUEBAS DE ERRORES ")
    try:
        err1 = Circumference(-3)
    except ValueError as e:
        print("Error detectado (circunferencia):", e)


