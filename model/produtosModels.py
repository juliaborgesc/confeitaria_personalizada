from model.database import Database

class ProdutoModel: #NÃO MEXI AINDA
    def __init__(self):
        self.db = Database()

    def obter_produtos(self):
        conexao = self.db.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        cursor.close()
        conexao.close()
        return produtos