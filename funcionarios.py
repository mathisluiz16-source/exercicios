class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


class Gerente(Funcionario):
    def calcular_salario(self):
        return self.salario_base * 1.20  # bônus de 20%


class Estagiario(Funcionario):
    def calcular_salario(self):
        return self.salario_base  # sem bônus


estagiario = Estagiario("João", 1000)
gerente = Gerente("Maria", 5000)

print(f"Estagiário {estagiario.nome}: R$ {estagiario.calcular_salario():.2f}")
print(f"Gerente {gerente.nome}: R$ {gerente.calcular_salario():.2f}")