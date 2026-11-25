import math

class Figura:
    def calcular_area(self):
        raise NotImplementedError("Subclasses devem implementar calcular_area()")


class Retangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Circulo(Figura):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2


# Polimorfismo: lista com figuras mistas
figuras = [
    Retangulo(5, 3),
    Circulo(2),
    Retangulo(4, 4),
    Circulo(1.5),
]

for f in figuras:
    print(f"{type(f).__name__}: área = {f.calcular_area():.2f}")

total = sum(f.calcular_area() for f in figuras)
print(f"Área total: {total:.2f}")