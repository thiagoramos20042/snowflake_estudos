# Snowflake | Conexão e exploração de tabelas

Script de conexão com Snowflake que lista tabelas de um schema e organiza o retorno em um DataFrame.

**Dados e integrações de apoio** · Script de laboratório

[← Data Science, IA e Automações · Thiago Oliveira](https://github.com/thiagoramos20042/thiagoramos20042) · [Catálogo de projetos](https://github.com/thiagoramos20042/thiagoramos20042/blob/main/PROJETOS.md)

## Objetivo

Praticar a configuração de uma conexão e a leitura de metadados de um ambiente Snowflake.

## O que você encontra

- Conexão parametrizada por usuário, conta, warehouse, database e schema.
- Consulta SHOW TABLES para listar tabelas.
- Exibição do resultado em um DataFrame no terminal.

## Tecnologias

Python · Snowflake Connector · pandas

## Arquivos principais

| Arquivo | Conteúdo |
| --- | --- |
| [arquivos/snowflake2.py](arquivos/snowflake2.py) | Script de conexão e consulta de tabelas. |
| [requirements.txt](requirements.txt) | Dependências do ambiente original. |

## Como explorar

Configure os parâmetros de conexão em arquivos/snowflake2.py com uma conta própria. Na raiz:

```bash
python -m pip install snowflake-connector-python pandas
python arquivos/snowflake2.py
```

## Contexto do projeto

O código versionado é executado no terminal. A descrição anterior mencionava uma interface Streamlit que não consta no script atual.

---

Integra o [portfólio de Thiago Oliveira](https://github.com/thiagoramos20042).
