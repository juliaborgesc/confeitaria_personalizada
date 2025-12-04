from database.conexao import Database

class Produto(): 
    def __init__(self, nome: str, descricao: str, valor_base: float, status_disponibilidade: bool, id_produto: int):
        self.nome = nome
        self.descricao = descricao
        self.valor_base = valor_base
        self.status_disponibilidade = status_disponibilidade
        self.id_produto = id_produto

    def __str__(self):
        return f"{self.id_produto} - {self.nome} (R${self.valor_base})"