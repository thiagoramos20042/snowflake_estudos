# Instalar o conector do Snowflake
import snowflake.connector
import pandas as pd

# 🔐 Credenciais
user = "thiagoramos20042"
password = "Thi@go58342131"
account = "oixoldc-ns82603"
warehouse = "COMPUTE_WH"
database = "DADOS_VENDAS"
schema = "VENDAS"

try:
    # Conexão com o Snowflake
    conn = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema
    )

    print("✅ Conectado com sucesso ao Snowflake!")

    # Criar cursor e executar comando
    cur = conn.cursor()
    cur.execute("SHOW TABLES")

    # Obter resultados e converter para DataFrame
    results = cur.fetchall()
    columns = [col[0] for col in cur.description]
    df = pd.DataFrame(results, columns=columns)

    # Mostrar resultado
    print("📋 Tabelas disponíveis no schema:")
    print(df)

    cur.close()
    conn.close()

except Exception as e:
    print(f"❌ Erro de conexão: {e}")
