from repository.produtoRepository import ProdutoRepository
from repository.ingredientesRepository import IngredientesRepository
from model.produtoModel import Produto
from model.produtoPersonalizavelModel import ProdutoPersonalizavel
from model.produtoNaoPersonalizavelModel import ProdutoNaoPersonalizavel

class ProdutosController:
    def __init__(self, db):
        self.repo = ProdutoRepository(db)
        self.ingredientes_repo = IngredientesRepository(db)

    # ==================== PRODUTOS PERSONALIZÁVEIS ====================
    def menu_personalizaveis(self):
        while True:
            print("\n" + "="*50)
            print("   PRODUTOS PERSONALIZÁVEIS")
            print("="*50)
            print("1 - Listar todos")
            print("2 - Buscar por ID")
            print("3 - Inserir novo produto personalizável")
            print("4 - Atualizar produto personalizável")
            print("5 - Deletar produto")
            print("0 - Voltar")
            print("="*50)
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.listar_personalizaveis()
            elif opcao == "2":
                self.buscar_personalizavel()
            elif opcao == "3":
                self.inserir_personalizavel()
            elif opcao == "4":
                self.atualizar_personalizavel()
            elif opcao == "5":
                self.deletar_produto()
            elif opcao == "0":
                break
            else:
                print("\n Opção inválida!")

    def listar_personalizaveis(self):
        print("\n--- PRODUTOS PERSONALIZÁVEIS ---")
        produtos = self.repo.listar_personalizaveis()
        if not produtos:
            print("Nenhum produto cadastrado.")
            return
        for p in produtos:
            print(f"\nID: {p.id_produto} | Nome: {p.nome}")
            print(f"Valor Base: R$ {p.valor_base:.2f} | Valor Final: R$ {p.valor_final:.2f}")
            print(f"Tamanho: {p.tamanho}")
            print(f"Status: {' Disponível' if p.status_disponibilidade else 'Indisponível'}")

    def buscar_personalizavel(self):
        id_produto = input("\nDigite o ID do produto: ").strip()
        produto = self.repo.buscar_personalizavel_por_id(id_produto)
        if produto:
            print(f"\n{'='*50}")
            print(f"ID: {produto.id_produto}")
            print(f"Nome: {produto.nome}")
            print(f"Descrição: {produto.descricao}")
            print(f"Valor Base: R$ {produto.valor_base:.2f}")
            print(f"Valor Final: R$ {produto.valor_final:.2f}")
            print(f"Tamanho: {produto.tamanho}")
            print(f"Status: {' Disponível' if produto.status_disponibilidade else ' Indisponível'}")
            print(f"Massa: {produto.fk_massa}")
            print(f"Recheio 1: {produto.fk_recheio1}")
            print(f"Recheio 2: {produto.fk_recheio2}")
            print(f"Cobertura: {produto.fk_cobertura}")
            print(f"Topping: {produto.fk_topping if produto.fk_topping else 'Nenhum'}")
            print(f"{'='*50}")
        else:
            print("\n Produto não encontrado!")

    def inserir_personalizavel(self):
        print("\n--- INSERIR PRODUTO PERSONALIZÁVEL ---")
        id_produto = input("ID do produto: ").strip()
        nome = input("Nome: ").strip()
        descricao = input("Descrição: ").strip()
        valor_base = float(input("Valor base: ").strip())
        valor_final = float(input("Valor final: ").strip())
        status = input("Disponível? (s/n): ").strip().lower() == 's'
        
        # Selecionar tamanho
        print("\n--- Tamanhos disponíveis ---")
        print("P | M | G")
        tamanho = input("Escolha o tamanho: ").strip().upper()
        
        # Selecionar ingredientes
        print("\n--- Massas disponíveis ---")
        massas = self.ingredientes_repo.listar_massas()
        for i, m in enumerate(massas, 1):
            print(f"{i} - {m.nome} (ID: {m.id_massa})")
        idx_massa = int(input("Escolha a massa: ").strip()) - 1
        fk_massa = massas[idx_massa].id_massa
        
        print("\n--- Recheios disponíveis ---")
        recheios = self.ingredientes_repo.listar_recheios()
        for i, r in enumerate(recheios, 1):
            print(f"{i} - {r.nome} (ID: {r.id_recheio})")
        idx_r1 = int(input("Escolha o recheio 1: ").strip()) - 1
        fk_recheio1 = recheios[idx_r1].id_recheio
        idx_r2 = int(input("Escolha o recheio 2: ").strip()) - 1
        fk_recheio2 = recheios[idx_r2].id_recheio
        
        print("\n--- Coberturas disponíveis ---")
        coberturas = self.ingredientes_repo.listar_coberturas()
        for i, c in enumerate(coberturas, 1):
            print(f"{i} - {c.nome} (ID: {c.id_cobertura})")
        idx_cob = int(input("Escolha a cobertura: ").strip()) - 1
        fk_cobertura = coberturas[idx_cob].id_cobertura
        
        print("\n--- Toppings disponíveis ---")
        toppings = self.ingredientes_repo.listar_toppings()
        print("0 - Nenhum")
        for i, t in enumerate(toppings, 1):
            print(f"{i} - {t.nome} (ID: {t.id_topping})")
        idx_top = int(input("Escolha o topping: ").strip())
        fk_topping = toppings[idx_top - 1].id_topping if idx_top > 0 else None
        
        produto = ProdutoPersonalizavel(
            id_produto, nome, descricao, valor_base, status,
            valor_final, tamanho, fk_massa, fk_recheio1, fk_recheio2, fk_cobertura, fk_topping
        )
        
        try:
            self.repo.inserir_personalizavel(produto)
            print("\n✓ Produto personalizável inserido com sucesso!")
        except Exception as e:
            print(f"\n Erro ao inserir produto: {e}")

    def atualizar_personalizavel(self):
        print("\n--- ATUALIZAR PRODUTO PERSONALIZÁVEL ---")
        id_produto = input("ID do produto: ").strip()
        produto = self.repo.buscar_personalizavel_por_id(id_produto)
        
        if not produto:
            print("\n Produto não encontrado!")
            return
        
        print(f"\nDados atuais: {produto.nome} | R$ {produto.valor_final:.2f}")
        nome = input("Novo nome (Enter para manter): ").strip() or produto.nome
        descricao = input("Nova descrição (Enter para manter): ").strip() or produto.descricao
        
        valor_base_input = input("Novo valor base (Enter para manter): ").strip()
        valor_base = float(valor_base_input) if valor_base_input else produto.valor_base
        
        valor_final_input = input("Novo valor final (Enter para manter): ").strip()
        valor_final = float(valor_final_input) if valor_final_input else produto.valor_final
        
        status_input = input("Disponível? (s/n/Enter para manter): ").strip().lower()
        status = produto.status_disponibilidade if status_input == '' else (status_input == 's')
        
        produto_atualizado = ProdutoPersonalizavel(
            id_produto, nome, descricao, valor_base, status,
            valor_final, produto.tamanho, produto.fk_massa, produto.fk_recheio1,
            produto.fk_recheio2, produto.fk_cobertura, produto.fk_topping
        )
        
        try:
            self.repo.atualizar_personalizavel(produto_atualizado)
            print("\n Produto atualizado com sucesso!")
        except Exception as e:
            print(f"\n Erro ao atualizar produto: {e}")

    def deletar_produto(self):
        id_produto = input("\nDigite o ID do produto a deletar: ").strip()
        confirma = input(f"Confirma a exclusão do produto '{id_produto}'? (s/n): ").strip().lower()
        
        if confirma == 's':
            try:
                self.repo.deletar_produto(id_produto)
                print("\n✓ Produto deletado com sucesso!")
            except Exception as e:
                print(f"\n Erro ao deletar produto: {e}")
        else:
            print("\nOperação cancelada.")

    # ==================== PRODUTOS NÃO PERSONALIZÁVEIS ====================
    def menu_nao_personalizaveis(self):
        while True:
            print("\n" + "="*50)
            print("   PRODUTOS NÃO PERSONALIZÁVEIS")
            print("="*50)
            print("1 - Listar todos")
            print("2 - Buscar por ID")
            print("3 - Inserir novo produto não personalizável")
            print("4 - Atualizar produto")
            print("5 - Deletar produto")
            print("0 - Voltar")
            print("="*50)
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.listar_nao_personalizaveis()
            elif opcao == "2":
                self.buscar_nao_personalizavel()
            elif opcao == "3":
                self.inserir_nao_personalizavel()
            elif opcao == "4":
                self.atualizar_nao_personalizavel()
            elif opcao == "5":
                self.deletar_produto()
            elif opcao == "0":
                break
            else:
                print("\n Opção inválida!")

    def listar_nao_personalizaveis(self):
        print("\n--- PRODUTOS NÃO PERSONALIZÁVEIS ---")
        produtos = self.repo.listar_nao_personalizaveis()
        if not produtos:
            print("Nenhum produto cadastrado.")
            return
        for p in produtos:
            print(f"\nID: {p.id_produto} | Nome: {p.nome}")
            print(f"Valor: R$ {p.valor_base:.2f}")
            print(f"Status: {' Disponível' if p.status_disponibilidade else ' Indisponível'}")

    def buscar_nao_personalizavel(self):
        id_produto = input("\nDigite o ID do produto: ").strip()
        produto = self.repo.buscar_nao_personalizavel_por_id(id_produto)
        if produto:
            print(f"\n{'='*50}")
            print(f"ID: {produto.id_produto}")
            print(f"Nome: {produto.nome}")
            print(f"Descrição: {produto.descricao}")
            print(f"Valor: R$ {produto.valor_base:.2f}")
            print(f"Status: {' Disponível' if produto.status_disponibilidade else ' Indisponível'}")
            print(f"{'='*50}")
        else:
            print("\n Produto não encontrado!")

    def inserir_nao_personalizavel(self):
        print("\n--- INSERIR PRODUTO NÃO PERSONALIZÁVEL ---")
        id_produto = input("ID do produto: ").strip()
        nome = input("Nome: ").strip()
        descricao = input("Descrição: ").strip()
        valor_base = float(input("Valor: ").strip())
        status = input("Disponível? (s/n): ").strip().lower() == 's'
        
        produto = ProdutoNaoPersonalizavel(id_produto, nome, descricao, valor_base, status)
        
        try:
            self.repo.inserir_nao_personalizavel(produto)
            print("\n✓ Produto não personalizável inserido com sucesso!")
        except Exception as e:
            print(f"\n Erro ao inserir produto: {e}")

    def atualizar_nao_personalizavel(self):
        print("\n--- ATUALIZAR PRODUTO NÃO PERSONALIZÁVEL ---")
        id_produto = input("ID do produto: ").strip()
        produto = self.repo.buscar_nao_personalizavel_por_id(id_produto)
        
        if not produto:
            print("\n Produto não encontrado!")
            return
        
        print(f"\nDados atuais: {produto.nome} | R$ {produto.valor_base:.2f}")
        nome = input("Novo nome (Enter para manter): ").strip() or produto.nome
        descricao = input("Nova descrição (Enter para manter): ").strip() or produto.descricao
        
        valor_input = input("Novo valor (Enter para manter): ").strip()
        valor_base = float(valor_input) if valor_input else produto.valor_base
        
        status_input = input("Disponível? (s/n/Enter para manter): ").strip().lower()
        status = produto.status_disponibilidade if status_input == '' else (status_input == 's')
        
        produto_atualizado = ProdutoNaoPersonalizavel(id_produto, nome, descricao, valor_base, status)
        
        try:
            self.repo.atualizar_nao_personalizavel(produto_atualizado)
            print("\n Produto atualizado com sucesso!")
        except Exception as e:
            print(f"\n Erro ao atualizar produto: {e}")
