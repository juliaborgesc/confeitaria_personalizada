from model.database import Database

db = Database()

try:
    con = db.conectar()
    print("Conexão realizada com sucesso!")
    con.close()
except Exception as e:
    print("Erro ao conectar:", e)
