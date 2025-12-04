from model.ingredientesModel import Massa, Recheio, Topping, Cobertura

class IngredientesRepository:
    def __init__(self, db):
        self.db = db

    # Massas:
    def criar_massa(self, massa: Massa) -> str | None:
        query = """INSERT INTO massa (nome, status_disponibilidade)
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
        query = "DELETE FROM massa WHERE id_massa = %s"
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(query, (id_massa,))
        conn.commit()
        cursor.close()

        return None
    
    def atualizar_massa(self, massa: Massa) -> None:
        query = """
            UPDATE massa
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

        cursor.execute("SELECT nome, status_disponibilidade FROM massa")
        linhas = cursor.fetchall()

        cursor.close()
        return [Massa(nome, status) for (nome, status) in linhas]

    # Recheios:
    def criar_recheio(self, recheio: Recheio) -> str:
        query = """
            INSERT INTO recheio (nome, status_disponibilidade, valor_adicional)
            VALUES (%s, %s, %s)
            RETURNING id_recheio
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            recheio.nome,
            recheio.status_disponibilidade,
            recheio.valor_adicional
        ))
        novo_id = cursor.fetchone()[0]
        conn.commit()

        cursor.close()
        return novo_id
    
    def apagar_recheio(self, id_recheio: str) -> None:
        query = "DELETE FROM recheio WHERE id_recheio = %s"
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(query, (id_recheio,))
        conn.commit()
        cursor.close()

        return None
    
    def atualizar_recheio(self, recheio: Recheio) -> None:
        query = """
            UPDATE recheio
            SET nome = %s,
                status_disponibilidade = %s,
                valor_adicional = %s
            WHERE id_recheio = %s
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            recheio.nome,
            recheio.status_disponibilidade,
            recheio.valor_adicional,
            recheio.id_recheio
        ))
        conn.commit()
        cursor.close()
        
        return None
    
    def listar_recheios(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT nome, status_disponibilidade, valor_adicional FROM recheio")
        linhas = cursor.fetchall()

        cursor.close()
        return [Recheio(nome, status, valor) for (nome, status, valor) in linhas]

    # Toppings:
    def criar_topping(self, topping: Topping) -> str:
        query = """
            INSERT INTO topping (nome, status_disponibilidade)
            VALUES (%s, %s)
            RETURNING id_topping
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            topping.nome,
            topping.status_disponibilidade
        ))
        novo_id = cursor.fetchone()[0]
        conn.commit()

        cursor.close()
        return novo_id
    
    def apagar_topping(self, id_topping: str) -> None:
        query = "DELETE FROM topping WHERE id_topping = %s"
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(query, (id_topping,))
        conn.commit()
        cursor.close()

        return None
    
    def atualizar_topping(self, topping: Topping) -> None:
        query = """
            UPDATE topping
            SET nome = %s,
                status_disponibilidade = %s
            WHERE id_topping = %s
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            topping.nome,
            topping.status_disponibilidade,
            topping.id_topping
        ))
        conn.commit()
        cursor.close()
        
        return None
    
    def listar_toppings(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT nome, status_disponibilidade FROM topping")
        linhas = cursor.fetchall()

        cursor.close()
        return [Topping(nome, status) for (nome, status) in linhas]

    # Coberturas:
    def criar_cobertura(self, cobertura: Cobertura) -> str:
        query = """
            INSERT INTO cobertura (nome, status_disponibilidade)
            VALUES (%s, %s)
            RETURNING id_cobertura
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            cobertura.nome,
            cobertura.status_disponibilidade
        ))
        novo_id = cursor.fetchone()[0]
        conn.commit()

        cursor.close()
        return novo_id
    
    def apagar_cobertura(self, id_cobertura: str) -> None:
        query = "DELETE FROM coberturas WHERE id_cobertura = %s"
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(query, (id_cobertura,))
        conn.commit()
        cursor.close()

        return None
    
    def atualizar_cobertura(self, cobertura: Cobertura) -> None:
        query = """
            UPDATE cobertura
            SET nome = %s,
                status_disponibilidade = %s
            WHERE id_cobertura = %s
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            cobertura.nome,
            cobertura.status_disponibilidade,
            cobertura.id_cobertura
        ))
        conn.commit()
        cursor.close()
        
        return None
    
    def listar_coberturas(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT nome, status_disponibilidade FROM cobertura")
        linhas = cursor.fetchall()

        cursor.close()
        return [Cobertura(nome, status) for (nome, status) in linhas]
