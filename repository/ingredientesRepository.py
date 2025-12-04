from model.ingredientesModel import Massa, Recheio, Topping, Cobertura

class IngredientesRepository:
    def __init__(self, db):
        self.db = db

    # Massas:
    def criar_massa(self, massa: Massa) -> str:
        query = """
            INSERT INTO massas (nome, status_disponibilidade)
            VALUES (%s, %s)
            RETURNING id_massa
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            massa.nome,
            massa.status_disponibilidade
        ))

        novo_id = cursor.fetchone()[0]
        conn.commit()

        cursor.close()
        return novo_id
    
    def apagar_massa(self, id_massa: str) -> None:
        query = "DELETE FROM massas WHERE id_massa = %s"
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(query, (id_massa,))
        conn.commit()
        cursor.close()

        return None
    
    def atualizar_massa(self, massa: Massa) -> None:
        query = """
            UPDATE massas
            SET nome = %s,
                status_disponibilidade = %s
            WHERE id_massa = %s
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            massa.nome,
            massa.status_disponibilidade,
            massa.id_massa
        ))
        conn.commit()
        cursor.close()
        
        return None
    
    def listar_massas(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT nome, status_disponibilidade FROM massas")
        linhas = cursor.fetchall()

        cursor.close()
        return [Massa(nome, status) for (nome, status) in linhas]

    # Recheios:
    def listar_recheios(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT nome, status_disponibilidade, valor_adicional FROM recheios")
        linhas = cursor.fetchall()

        cursor.close()
        return [Recheio(nome, status, valor) for (nome, status, valor) in linhas]

    # Toppings:
    def listar_toppings(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT nome, status_disponibilidade FROM toppings")
        linhas = cursor.fetchall()

        cursor.close()
        return [Topping(nome, status) for (nome, status) in linhas]

    # Coberturas:
    def listar_coberturas(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT nome, status_disponibilidade FROM coberturas")
        linhas = cursor.fetchall()

        cursor.close()
        return [Cobertura(nome, status) for (nome, status) in linhas]
