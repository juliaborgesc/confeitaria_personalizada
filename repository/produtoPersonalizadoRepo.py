from model.produtoPersonalizavelModel import ProdutoPersonalizavel
from model.ingredientesModel import Massa, Recheio, Topping, Cobertura
from database.conexao import Database

class ProdutoPersonalizadoRepository:
    def __init__(self, db: Database):
        self.db = db

    def listar_todos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
        SELECT 
            p.id_produto, p.nome, p.descricao, p.valor_base, p.status_disponibilidade,
            pp.valor_final, pp.tamanho,
            m.nome AS massa,
            r1.nome AS recheio1,
            r2.nome AS recheio2,
            c.nome AS cobertura,
            t.nome AS topping
        FROM produtos p
        JOIN produto_personalizavel pp ON p.id_produto = pp.fk_produto_id_produto
        JOIN massas m ON pp.fk_massa = m.id_massa
        JOIN recheios r1 ON pp.fk_recheio1 = r1.id_recheio
        JOIN recheios r2 ON pp.fk_recheio2 = r2.id_recheio
        JOIN coberturas c ON pp.fk_cobertura = c.id_cobertura
        JOIN toppings t ON pp.fk_topping = t.id_topping
        ORDER BY p.id_produto;
        """

        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        produtos = []
        for row in rows:
            (id_prod, nome, descricao, valor_base, status,
             valor_final, tamanho, massa, recheio1, recheio2,
             cobertura, topping) = row

            produto = ProdutoPersonalizavel(
                id_produto=id_prod,
                nome=nome,
                descricao=descricao,
                valor_base=valor_base,
                status_disponibilidade=status,
                valor_final=valor_final,
                massa=Massa(massa, True),
                recheio1=Recheio(recheio1, True, 0),
                recheio2=Recheio(recheio2, True, 0),
                cobertura=Cobertura(cobertura, True),
                topping=Topping(topping, True),
                tamanho=tamanho
            )

            produtos.append(produto)

        return produtos