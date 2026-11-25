
class Veiculo:
    def __init__(self, marca, velocidade_max):
        self.marca = marca
        self.velocidade_max = velocidade_max

    def mover(self):
        print(f"O veículo {self.marca} está se movendo.")


class Carro(Veiculo):
    def __init__(self, marca, velocidade_max, num_portas):
        super().__init__(marca, velocidade_max)
        self.num_portas = num_portas

    def mover(self):
        print(f"O carro {self.marca} ({self.num_portas} portas) está acelerando "
              f"até {self.velocidade_max} km/h.")


class Bicicleta(Veiculo):
    def __init__(self, marca, velocidade_max, num_marchas):
        super().__init__(marca, velocidade_max)
        self.num_marchas = num_marchas

    def mover(self):
        print(f"A bicicleta {self.marca} ({self.num_marchas} marchas) está sendo "
              f"pedalada a até {self.velocidade_max} km/h.")


# Teste
veiculos = [
    Veiculo("Genérico", 100),
    Carro("Toyota", 180, 4),
    Bicicleta("Caloi", 35, 21),
]

for v in veiculos:
    v.mover()