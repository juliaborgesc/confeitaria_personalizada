from model.produtoNaoPersonalizavelModel import Bebidas, BoloPronto, ItensFesta


# QUASE CERTEZA QUE ISSO TA ERRADO
class BebidasRepository:
    def __init__(self, db):
        self.db = db

    def listar_bebidas(self) -> list[Bebidas]:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        query = """
        SELECT 
            p.id_produto,
            p.nome,
            p.descricao,
            p.valor_base,
            p.status_disponibilidade
        FROM produto p
        JOIN produto_naopersonalizavel np 
            ON np.fk_produto_id_produto = p.id_produto
        JOIN bebidas b
            ON b.fk_produto_naopersonalizavel = p.id_produto;
        """
        
        cursor.execute(query)
        linhas = cursor.fetchall()
        cursor.close()

        return [Bebidas(*linha) for linha in linhas]
    
    def buscar_por_id(self, id_produto: str) -> Bebidas | None:
        conn = self.db.get_connection()
        cursor = conn.cursor()

        query = """
        SELECT 
            p.id_produto,
            p.nome,
            p.descricao,
            p.valor_base,
            p.status_disponibilidade
        FROM produto p
        JOIN produto_naopersonalizavel np 
            ON np.fk_produto_id_produto = p.id_produto
        JOIN bebidas b
            ON b.fk_produto_naopersonalizavel = p.id_produto
        WHERE p.id_produto = %s;
        """

        cursor.execute(query, (id_produto,))
        linha = cursor.fetchone()
        cursor.close()

        return Bebidas(*linha) if linha else None
    
    def inserir_bebida(self, bebida: Bebidas) -> str:
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO produto (id_produto, nome, descricao, valor_base, status_disponibilidade)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id_produto;
        """, (
            bebida.id_produto,
            bebida.nome,
            bebida.descricao,
            bebida.valor_base,
            bebida.status_disponibilidade,
        ))
        id_produto = cursor.fetchone()[0]

        cursor.execute("""
            INSERT INTO produto_naopersonalizavel (fk_produto_id_produto)
            VALUES (%s);
        """, (id_produto,))

        cursor.execute("""
            INSERT INTO bebidas (fk_produto_naopersonalizavel)
            VALUES (%s);
        """, (id_produto,))

        conn.commit()
        cursor.close()
        return id_produto