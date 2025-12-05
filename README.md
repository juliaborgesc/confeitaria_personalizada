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
