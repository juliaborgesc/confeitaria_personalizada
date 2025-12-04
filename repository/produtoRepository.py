from model.produtoModel import Produto

class ProdutoRepository:
    def __init__(self, db):
        self.db = db

    def criar_produto(self, produto: Produto) -> str:
        query = """
            INSERT INTO produtos (nome, descricao, valor_base, status_disponibilidade)
            VALUES (%s, %s, %s, %s)
            RETURNING id_produto
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            produto.nome,
            produto.descricao,
            produto.valor_base,
            produto.status_disponibilidade
        ))

        novo_id = cursor.fetchone()[0]
        conn.commit()

        cursor.close()
        return novo_id

    def listar_produtos(self) -> list[Produto]:
        query = """
            SELECT id_produto, nome, descricao, valor_base, status_disponibilidade
            FROM produtos
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query)
        produtos = cursor.fetchall()

        cursor.close()

        return [Produto(*linha) for linha in produtos]

    def buscar_produto(self, id_produto: int) -> Produto:
        query = """
            SELECT id_produto, nome, descricao, valor_base, status_disponibilidade
            FROM produtos
            WHERE id_produto = %s
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (id_produto,))
        linha = cursor.fetchone()

        cursor.close()

        return Produto(*linha) if linha else None

    def atualizar_produto(self, produto: Produto) -> None:
        query = """
            UPDATE produtos
            SET nome = %s,
                descricao = %s,
                valor_base = %s,
                status_disponibilidade = %s
            WHERE id_produto = %s
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            produto.nome,
            produto.descricao,
            produto.valor_base,
            produto.status_disponibilidade,
            produto.id_produto
        ))

        conn.commit()
        cursor.close()

    def excluir_produto(self, id_produto: int) -> None:
        query = "DELETE FROM produtos WHERE id_produto = %s"

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (id_produto,))
        conn.commit()

        cursor.close()
