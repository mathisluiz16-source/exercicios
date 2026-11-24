class produto:
    def __init__(self, categoria, estoque, nome, preco, produto_id=None):
        self.categoria = categoria
        self.estoque = estoque
        self.nome = nome
        self.preco = preco
        self.produto_id = produto_id

    def exibir(self):
        print(f'Categoria: {self.categoria}')
        print(f'Estoque: {self.estoque}')
        print(f'Nome: {self.nome}')
        print(f'Preço: {self.preco}')

    def valor_total(self):
        return self.estoque * self.preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
        return self.preco

    def vender(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            print("Estoque insuficiente para a venda.")
            return False

    def repor_estoque(self, quantidade):
        self.estoque += quantidade
        return self.estoque


p1 = produto("Eletrônicos", 10, "Smartphone", 1500.00)
p2 = produto("Eletrodomésticos", 5, "Geladeira", 2500.00)

p1.exibir()
p2.exibir()

p1.aplicar_desconto(10)
print(f'Preço com desconto do {p1.nome}: {p1.preco}')
p2.vender(3)
print(f'Estoque restante do {p2.nome}: {p2.estoque}')
p1.repor_estoque(5)
print(f'Estoque atualizado do {p1.nome}: {p1.estoque}')

print(f'Valor total do estoque do {p1.nome}: {p1.valor_total()}')
print(f'Valor total do estoque do {p2.nome}: {p2.valor_total()}')