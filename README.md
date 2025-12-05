# Confeitaria Personalizada

## Como testar a conexão e os repositórios

1. **Abra um terminal na raiz do projeto** (a pasta que contém este README). Se baixou o projeto via ZIP, extraia e entre na pasta
   `confeitaria_personalizada` antes de rodar qualquer comando.

2. **Crie o ambiente virtual e instale as dependências**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente**. Copie o arquivo `.env.example` para `.env` (na raiz) e ajuste os valores, ou use o
   exemplo do Supabase fornecido:
   ```bash
   cp .env.example .env
   # edite .env se precisar trocar host/usuário/senha/porta
   ```

4. **Garanta que o esquema esteja criado** executando o script SQL contra o banco (rode no mesmo terminal, ainda na raiz):
   ```bash
   psql \
     -h "$SUPABASE_HOST" \
     -d "$SUPABASE_DB" \
     -U "$SUPABASE_USER" \
     -p "$SUPABASE_PORT" \
     -f database/schema.sql
   ```

5. **Rode o teste de fumaça dos ingredientes** para verificar inserção, listagem e limpeza:
   ```bash
   python scripts/smoke_test_ingredientes.py
   ```

O script cria uma massa temporária, confirma que ela aparece na listagem e depois a apaga, permitindo validar rapidamente se as
operações básicas do repositório estão funcionando com o banco configurado.

## Onde encontrar as mudanças feitas

Todas as alterações anteriores estão no próprio repositório, nos arquivos abaixo (abra-os no editor ou visualize pelo GitHub
após enviar/atualizar o branch):

- `database/conexao.py`: helper para abrir conexão usando as variáveis de ambiente.
- `database/schema.sql`: definição completa das tabelas usadas pelo app.
- `repository/ingredientesRepository.py`: ajustes nos CRUDs para massa, recheio e cobertura.
- `scripts/smoke_test_ingredientes.py`: roteiro simples para inserir/listar/remover uma massa de teste.
- `.env.example`: exemplo das variáveis Supabase para copiar para `.env`.

Se você clonar ou baixar o projeto, essas mudanças já estão na árvore de código e podem ser vistas localmente sem precisar
esperar aparecer no GitHub.

## Como enviar as mudanças para o GitHub

Se ao abrir o repositório online você não vê nada novo, é porque o branch local `work` ainda não foi enviado. Para publicar
as alterações no GitHub:

1. **Confirme qual remoto está configurado** (o comando deve listar `origin` apontando para o repositório desejado):
   ```bash
   git remote -v
   ```
   - Se não existir nenhum remoto, adicione-o (substitua pela URL do seu fork, caso use outro usuário):
     ```bash
     git remote add origin https://github.com/livia-rosario/confeitaria_personalizada.git
     ```

2. **Envie o branch `work`** com as atualizações:
   ```bash
   git push -u origin work
   ```
   - Se aparecer `error: failed to push some refs`, primeiro baixe o histórico remoto e tente de novo:
     ```bash
     git pull --rebase origin work
     git push origin work
     ```
   - Caso o branch remoto não exista ainda, o primeiro `git push -u origin work` deve criá-lo. O `-u` configura o upstream,
     permitindo usar apenas `git push` ou `git pull` nos próximos envios.

Depois disso, recarregue a página do repositório ou abra um Pull Request a partir do branch `work` para que o GitHub mostre
os commits recentes.
