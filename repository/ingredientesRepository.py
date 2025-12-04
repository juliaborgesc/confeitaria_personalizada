from model.ingredientesModel import Massa, Recheio, Topping, Cobertura

class IngredientesRepository:
    def __init__(self, db):
        self.db = db

    # Aqui vocês acham que precisa criar mais métodos para cada tipo de ingrediente??? não
    # Massas:
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
