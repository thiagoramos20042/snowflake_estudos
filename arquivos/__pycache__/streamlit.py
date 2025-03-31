import streamlit as st
import snowflake.connector
import pandas as pd

# Título da aplicação
st.title("🔗 Conexão com Snowflake")
st.write("Veja as tabelas disponíveis no schema especificado.")

# Entradas de credenciais
with st.sidebar:
    st.header("🔐 Credenciais")
    user = st.text_input("Usuário", value="thiagoramos20042")
    password = st.text_input("Senha", type="password")
    account = st.text_input("Conta", value="oixoldc-ns82603")
    warehouse = st.text_input("Warehouse", value="COMPUTE_WH")
    database = st.text_input("Database", value="DADOS_VENDAS")
    schema = st.text_input("Schema", value="VENDAS")
    conectar = st.button("Conectar")

# Ação de conexão
if conectar:
    try:
        # Conectar ao Snowflake
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )

        st.success("✅ Conectado com sucesso ao Snowflake!")

        # Criar cursor e buscar tabelas
        cur = conn.cursor()
        cur.execute("SHOW TABLES")

        results = cur.fetchall()
        columns = [col[0] for col in cur.description]
        df = pd.DataFrame(results, columns=columns)

        st.subheader("📋 Tabelas disponíveis no schema:")
        st.dataframe(df)

        cur.close()
        conn.close()

    except Exception as e:
        st.error(f"❌ Erro de conexão: {e}")
