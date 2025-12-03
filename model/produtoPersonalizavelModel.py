from model.produtoModel import Produto

class ProdutoPersonalizavel(Produto):
    def __init__(self, id_produto, nome, descricao, valor_base, status_disponibilidade,
                 valor_final, tamanho): #gente massa, recheio, topping e cobertura entram aonde???
        
        super().__init__(id_produto, nome, descricao, valor_base, status_disponibilidade)

        self.valor_final = valor_final
        self.tamanho = tamanho

        def __str__(self):
            return f"{self.id_produto} - {self.nome} (R${self.valor_final}) - Tamanho: {self.tamanho}"