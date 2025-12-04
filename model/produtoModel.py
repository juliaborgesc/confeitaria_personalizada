from model.database import Database
from abc import ABC, abstractmethod

class Produto(): 
    def __init__(self, nome: str, descricao: str, valor_base: float, status_disponibilidade: bool, id_produto: int):
        self.nome = nome
        self.descricao = descricao
        self.valor_base = valor_base
        self.status_disponibilidade = status_disponibilidade
        self.id_produto = id_produto

    def criarProduto(self):
        pass
    def atualizarProduto(self):
        pass
    def deletarProduto(self):
        pass
    def buscarProduto(self, id_produto_buscado):
        pass
    def __str__(self):
        return f"{self.id_produto} - {self.nome} (R${self.valor_base})"