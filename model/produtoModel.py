from model.database import Database

class Produto: 
    def __init__(self, nome, descricao, valor_base, status_disponibilidade, id_produto):
        self.nome = nome
        self.descricao = descricao
        self.valor_base = valor_base
        self.status_disponibilidade = status_disponibilidade
        self.id_produto = id_produto

    def criarProduto(self):

    def atualizarProduto(self):

    def deletarProduto(self):
    
    def buscarProduto(self, id_produto):
    
    def __str__(self):
        return f"{self.id_produto} - {self.nome} (R${self.valor_base})"