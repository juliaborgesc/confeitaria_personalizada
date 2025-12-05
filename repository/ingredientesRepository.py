from uuid import uuid4

from model.ingredientesModel import Massa, Recheio, Topping, Cobertura

class IngredientesRepository:
    def __init__(self, db):
        self.db = db

    # Massas:
    def criar_massa(self, massa: Massa) -> str | None:
        novo_id = massa.id_massa or str(uuid4())
        query = """INSERT INTO massa (id_massa, nome, status_disponibilidade)
            VALUES (%s, %s, %s)
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            novo_id,
            massa.nome,
            massa.status_disponibilidade
        ))
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

        cursor.execute("SELECT id_massa, nome, status_disponibilidade FROM massa")
        linhas = cursor.fetchall()

        cursor.close()
        return [Massa(id_massa, nome, status) for (id_massa, nome, status) in linhas]

    # Recheios:
    def criar_recheio(self, recheio: Recheio) -> str:
        novo_id = recheio.id_recheio or str(uuid4())
        query = """
            INSERT INTO recheio (id_recheio, nome, status_disponibilidade, valor_adc)
            VALUES (%s, %s, %s, %s)
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            novo_id,
            recheio.nome,
            recheio.status_disponibilidade,
            recheio.valor_adc
        ))
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
                valor_adc = %s
            WHERE id_recheio = %s
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            recheio.nome,
            recheio.status_disponibilidade,
            recheio.valor_adc,
            recheio.id_recheio
        ))
        conn.commit()
        cursor.close()
        
        return None
    
    def listar_recheios(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id_recheio, nome, status_disponibilidade, valor_adc FROM recheio")
        linhas = cursor.fetchall()

        cursor.close()
        return [Recheio(id_recheio, nome, status, valor) for (id_recheio, nome, status, valor) in linhas]

    # Toppings:
    def criar_topping(self, topping: Topping) -> str:
        novo_id = topping.id_topping or str(uuid4())
        query = """
            INSERT INTO topping (id_topping, nome, status_disponibilidade, valor_adc)
            VALUES (%s, %s, %s, %s)
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            novo_id,
            topping.nome,
            topping.status_disponibilidade,
            topping.valor_adc
        ))
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
                status_disponibilidade = %s,
                valor_adc = %s
            WHERE id_topping = %s
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            topping.nome,
            topping.status_disponibilidade,
            topping.valor_adc,
            topping.id_topping
        ))
        conn.commit()
        cursor.close()
        
        return None
    
    def listar_toppings(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id_topping, nome, status_disponibilidade, valor_adc FROM topping")
        linhas = cursor.fetchall()

        cursor.close()
        return [Topping(id_topping, nome, status, valor_adc) for (id_topping, nome, status, valor_adc) in linhas]

    # Coberturas:
    def criar_cobertura(self, cobertura: Cobertura) -> str:
        novo_id = cobertura.id_cobertura or str(uuid4())
        query = """
            INSERT INTO cobertura (id_cobertura, nome, status_disponibilidade)
            VALUES (%s, %s, %s)
        """

        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(query, (
            novo_id,
            cobertura.nome,
            cobertura.status_disponibilidade
        ))
        conn.commit()

        cursor.close()
        return novo_id
    
    def apagar_cobertura(self, id_cobertura: str) -> None:
        query = "DELETE FROM cobertura WHERE id_cobertura = %s"
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

        cursor.execute("SELECT id_cobertura, nome, status_disponibilidade FROM cobertura")
        linhas = cursor.fetchall()

        cursor.close()
        return [Cobertura(id_cobertura, nome, status) for (id_cobertura, nome, status) in linhas]
