from model.produtoPersonalizavelModel import ProdutoPersonalizavel
from model.ingredientesModel import Massa, Recheio, Cobertura, Topping

class ProdutoView:
    def __init__(self, produto_repo, ingredientes_repo):
        self.produto_repo = produto_repo
        self.ingredientes_repo = ingredientes_repo

    def menu(self):
        while True:
            print("\n=== MENU PRODUTOS PERSONALIZÁVEIS ===")
            print("1 - Listar produtos")
            print("2 - Buscar por ID")
            print("3 - Criar novo produto personalizável")
            print("4 - Deletar produto")
            print("0 - Sair")
            opc = input("Escolha uma opção: ")

            if opc == "1":
                self.listar_produtos()
            elif opc == "2":
                self.buscar_por_id()
            elif opc == "3":
                self.criar_produto()
            elif opc == "4":
                self.deletar_produto()
            elif opc == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

    def listar_produtos(self):
        print("\n=== LISTA DE PRODUTOS PERSONALIZÁVEIS ===")
        produtos = self.produto_repo.listar_todos()

        if not produtos:
            print("Nenhum produto encontrado!")
            return

        for p in produtos:
            print(f"""
                    ID: {p.id_produto}
                    Nome: {p.nome}
                    Valor final: R$ {p.valor_final}
                    Tamanho: {p.tamanho}
                    Massa: {p.massa.nome}
                    Recheio 1: {p.recheio1.nome}
                    Recheio 2: {p.recheio2.nome}
                    Cobertura: {p.cobertura.nome}
                    Topping: {(p.topping.nome if p.topping else "Nenhum")}
                    ------------------------""")

    def buscar_por_id(self):
        print("\n=== CONSULTAR PRODUTO ===")
        idp = input("Digite o ID do produto: ")

        prod = self.produto_repo.buscar_por_id(idp)

        if prod is None:
            print("Produto não encontrado.")
            return

        print(f"""
                ==== DETALHES DO PRODUTO ====
                ID: {prod.id_produto}
                Nome: {prod.nome}
                Descrição: {prod.descricao}
                Valor base: R$ {prod.valor_base}
                Valor final: R$ {prod.valor_final}
                Status: {prod.status_disponibilidade}
                Tamanho: {prod.tamanho}

                Massa: {prod.massa.nome}
                Recheio 1: {prod.recheio1.nome}
                Recheio 2: {prod.recheio2.nome}
                Cobertura: {prod.cobertura.nome}
                Topping: {(prod.topping.nome if prod.topping else "Nenhum")}
                """)

    def criar_produto(self):
        print("\n=== CRIAR PRODUTO PERSONALIZÁVEL ===")

        nome = input("Nome do produto: ")
        descricao = input("Descrição: ")
        valor_base = float(input("Valor base: "))
        valor_final = float(input("Valor final: "))
        status = input("Status (ativo/inativo): ")

        print("\n--- Selecione o tamanho ---")
        tamanhos = ["P", "M", "G"]
        for i, t in enumerate(tamanhos):
            print(f"{i+1} - {t}")
        tamanho_escolha = int(input("Escolha: "))
        tamanho = tamanhos[tamanho_escolha - 1]

        print("\n--- Selecionar massa ---")
        massas = self.ingredientes_repo.listar_massas()
        for i, m in enumerate(massas):
            print(f"{i+1} - {m.nome}")
        massa = massas[int(input("Escolha: ")) - 1]

        print("\n--- Selecionar recheio 1 ---")
        recheios = self.ingredientes_repo.listar_recheios()
        for i, r in enumerate(recheios):
            print(f"{i+1} - {r.nome}")
        recheio1 = recheios[int(input("Escolha: ")) - 1]

        print("\n--- Selecionar recheio 2 ---")
        for i, r in enumerate(recheios):
            print(f"{i+1} - {r.nome}")
        recheio2 = recheios[int(input("Escolha: ")) - 1]

        print("\n--- Selecionar cobertura ---")
        coberturas = self.ingredientes_repo.listar_coberturas()
        for i, c in enumerate(coberturas):
            print(f"{i+1} - {c.nome}")
        cobertura = coberturas[int(input("Escolha: ")) - 1]

        print("\n--- Selecionar topping (opcional) ---")
        toppings = self.ingredientes_repo.listar_toppings()
        print("0 - Nenhum topping")
        for i, t in enumerate(toppings):
            print(f"{i+1} - {t.nome}")
        top = int(input("Escolha: "))
        topping = toppings[top - 1] if top != 0 else None

        novo_produto = ProdutoPersonalizavel(
            id_produto=None,
            nome=nome,
            descricao=descricao,
            valor_base=valor_base,
            status_disponibilidade=status,
            valor_final=valor_final,
            tamanho=tamanho,
            massa=massa,
            recheio1=recheio1,
            recheio2=recheio2,
            cobertura=cobertura,
            topping=topping
        )

        # Inserir no banco
        novo_id = self.produto_repo.inserir(novo_produto)
        print(f"\nProduto criado com sucesso! ID: {novo_id}")

    def deletar_produto(self):
        print("\n=== DELETAR PRODUTO ===")
        idp = input("ID do produto: ")

        self.produto_repo.deletar(idp)
        print("Produto deletado com sucesso!")
