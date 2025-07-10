import pandas as pd
from sqlalchemy import create_engine

# 1. Ler o arquivo CSV
df = pd.read_csv("vendas.csv")

# 2. Limpeza básica
df.dropna(inplace=True)
df['data'] = pd.to_datetime(df['data'])

# 3. Conexão com o MySQL
usuario = "root"         # ou o seu usuário do MySQL
senha = "password" # troque pela sua senha real
host = "localhost:3306"
banco = "vendas"

# Montar string de conexão
engine = engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/vendas")
conn = engine.connect()


# 4. Enviar dados para a tabela
df.to_sql("vendas_ecommerce", con=engine, if_exists="replace", index=False)


print("Dados importados com sucesso!")

