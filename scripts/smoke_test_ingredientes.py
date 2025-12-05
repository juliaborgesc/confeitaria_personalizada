"""Executa um teste simples de ida e volta nos ingredientes.

O script insere uma massa temporária, confirma a leitura de volta e
remove o registro para não sujar o banco.
"""

import os

from model.ingredientesModel import Massa
from repository.ingredientesRepository import IngredientesRepository
from database.conexao import Database


def main():
    required_envs = [
        "SUPABASE_HOST",
        "SUPABASE_DB",
        "SUPABASE_USER",
        "SUPABASE_PASSWORD",
        "SUPABASE_PORT",
    ]

    missing = [name for name in required_envs if not os.getenv(name)]
    if missing:
        print("Variáveis ausentes: " + ", ".join(missing))
        print("Crie um arquivo .env (pode copiar de .env.example) e rode novamente a partir da raiz do projeto.")
        return

    db = Database()
    conn = db.get_connection()

    if conn is None:
        print(
            "Não foi possível conectar ao banco. Confira as variáveis de ambiente e se o comando psql do passo 4 do README"
            " executou sem erros."
        )
        return

    repo = IngredientesRepository(db)
    massa_temporaria = Massa(
        id_massa=None,
        nome="Smoke test massa",
        status_disponibilidade=True,
    )

    massa_id = repo.criar_massa(massa_temporaria)
    print(f"Massa criada com id {massa_id}")

    massas = repo.listar_massas()
    encontrados = [m for m in massas if m.id_massa == massa_id]

    if encontrados:
        print("Massa encontrada na listagem, repositório funcionando.")
    else:
        print("Massa não encontrada na listagem! Verifique o repositório.")

    repo.apagar_massa(massa_id)
    print("Massa temporária removida.")


if __name__ == "__main__":
    main()
