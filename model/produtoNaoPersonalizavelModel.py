from model.produtoModel import Produto


class ProdutoNaoPersonalizavel(Produto):
    def __init__(self, id_produto, nome, descricao, valor_base, status_disponibilidade):
        
        super().__init__(id_produto, nome, descricao, valor_base, status_disponibilidade)

    def __str__(self):
        return f"{self.id_produto} - {self.nome} (R${self.valor_base})"