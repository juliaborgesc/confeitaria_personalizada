-- Schema for confeitaria_personalizada PostgreSQL database
-- Defines tables and constraints so that relational dependencies are respected.

-- Independent reference tables
CREATE TABLE IF NOT EXISTS cliente (
    cpf VARCHAR PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS massa (
    id_massa VARCHAR PRIMARY KEY,
    nome VARCHAR,
    status_disponibilidade BOOLEAN
);

CREATE TABLE IF NOT EXISTS recheio (
    id_recheio VARCHAR PRIMARY KEY,
    nome VARCHAR,
    valor_adc NUMERIC,
    status_disponibilidade BOOLEAN
);

CREATE TABLE IF NOT EXISTS cobertura (
    id_cobertura VARCHAR PRIMARY KEY,
    nome VARCHAR,
    status_disponibilidade BOOLEAN
);

CREATE TABLE IF NOT EXISTS topping (
    id_topping VARCHAR PRIMARY KEY,
    nome VARCHAR,
    status_disponibilidade BOOLEAN,
    valor_adc NUMERIC DEFAULT 0
);

CREATE TABLE IF NOT EXISTS tamanho (
    nome_tamanho VARCHAR PRIMARY KEY,
    valor_base NUMERIC,
    status_disponibilidade BOOLEAN
);

CREATE TABLE IF NOT EXISTS produto (
    id_produto VARCHAR PRIMARY KEY,
    nome VARCHAR,
    descricao VARCHAR,
    valor_base NUMERIC,
    status_disponibilidade BOOLEAN
);

-- Auxiliary key-value storage used by the application
CREATE TABLE IF NOT EXISTS kv_store_e586621a (
    key TEXT PRIMARY KEY,
    value JSONB NOT NULL
);

-- Non-personalized product specializations
CREATE TABLE IF NOT EXISTS produto_naopersonalizavel (
    fk_produto_id_produto VARCHAR PRIMARY KEY,
    CONSTRAINT fk_pnp_produto FOREIGN KEY (fk_produto_id_produto) REFERENCES produto (id_produto)
);

CREATE TABLE IF NOT EXISTS bebidas (
    fk_produto_naopersonalizavel VARCHAR PRIMARY KEY,
    CONSTRAINT fk_bebidas_pnp FOREIGN KEY (fk_produto_naopersonalizavel) REFERENCES produto_naopersonalizavel (fk_produto_id_produto)
);

CREATE TABLE IF NOT EXISTS bolo_pronto (
    fk_produto_naopersonalizavel VARCHAR PRIMARY KEY,
    CONSTRAINT fk_bolopronto_pnp FOREIGN KEY (fk_produto_naopersonalizavel) REFERENCES produto_naopersonalizavel (fk_produto_id_produto)
);

CREATE TABLE IF NOT EXISTS itens_festa (
    fk_produto_naopersonalizavel VARCHAR PRIMARY KEY,
    CONSTRAINT fk_itens_pnp FOREIGN KEY (fk_produto_naopersonalizavel) REFERENCES produto_naopersonalizavel (fk_produto_id_produto)
);

-- Personalized product specialization
CREATE TABLE IF NOT EXISTS produto_personalizavel (
    fk_produto_id_produto VARCHAR PRIMARY KEY,
    valor_final NUMERIC,
    fk_massa VARCHAR,
    fk_recheio1 VARCHAR,
    fk_recheio2 VARCHAR,
    fk_cobertura VARCHAR,
    fk_topping VARCHAR,
    fk_tamanho VARCHAR,
    CONSTRAINT fk_pp_produto FOREIGN KEY (fk_produto_id_produto) REFERENCES produto (id_produto),
    CONSTRAINT fk_pp_massa FOREIGN KEY (fk_massa) REFERENCES massa (id_massa),
    CONSTRAINT fk_pp_recheio1 FOREIGN KEY (fk_recheio1) REFERENCES recheio (id_recheio),
    CONSTRAINT fk_pp_recheio2 FOREIGN KEY (fk_recheio2) REFERENCES recheio (id_recheio),
    CONSTRAINT fk_pp_cobertura FOREIGN KEY (fk_cobertura) REFERENCES cobertura (id_cobertura),
    CONSTRAINT fk_pp_topping FOREIGN KEY (fk_topping) REFERENCES topping (id_topping),
    CONSTRAINT fk_pp_tamanho FOREIGN KEY (fk_tamanho) REFERENCES tamanho (nome_tamanho)
);

-- Orders and items
CREATE TABLE IF NOT EXISTS pedido (
    id_pedido VARCHAR PRIMARY KEY,
    status_pedido VARCHAR,
    valor_total NUMERIC,
    forma_pagamento VARCHAR,
    cod_nf VARCHAR,
    senha INTEGER,
    fk_cliente VARCHAR,
    data_hora_inicio TIMESTAMP WITHOUT TIME ZONE,
    data_hora_fim TIMESTAMP WITHOUT TIME ZONE,
    CONSTRAINT fk_pedido_cliente FOREIGN KEY (fk_cliente) REFERENCES cliente (cpf)
);

CREATE TABLE IF NOT EXISTS item_pedido (
    id_itempedido VARCHAR PRIMARY KEY,
    quantidade INTEGER,
    valor_item NUMERIC,
    fk_pedido VARCHAR,
    fk_produto VARCHAR,
    CONSTRAINT fk_itempedido_pedido FOREIGN KEY (fk_pedido) REFERENCES pedido (id_pedido),
    CONSTRAINT fk_itempedido_produto FOREIGN KEY (fk_produto) REFERENCES produto (id_produto)
);
