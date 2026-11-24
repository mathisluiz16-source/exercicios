class Livro:
    """Representa um livro de uma biblioteca."""

    def __init__(self, titulo, autor, paginas, disponivel=True):
        """
        Inicializa um livro.

        Args:
            titulo (str): título do livro.
            autor (str): autor do livro.
            paginas (int): quantidade de páginas.
            disponivel (bool): True se estiver disponível para empréstimo.
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = disponivel

    def descricao(self):
        """Exibe todas as informações do livro formatadas."""
        status = "Disponível" if self.disponivel else "Emprestado"
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")
        print(f"Disponibilidade: {status}")
        print("-" * 80)

    def emprestar(self):
        """Altera a disponibilidade do livro para False (emprestado)."""
        self.disponivel = False

    def devolver(self):
        """Altera a disponibilidade do livro para True (devolvido)."""
        self.disponivel = True


l1 = Livro("Dom Casmurro", "Machado de Assis", 256)
l2 = Livro("O Alquimista", "Paulo Coelho", 208)
l3 = Livro("Grande Sertão: Veredas", "Guimarães Rosa", 608)

l1.descricao()
l2.emprestar()
l2.descricao()
l2.devolver()
l2.descricao()

git add Livro.py
git commit -m "feat: implementa classe livro"
git push