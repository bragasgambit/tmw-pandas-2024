# %%
# .xlsx é um binário
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df
# Pode dar erro: Import Error - para importar .xlsx deve ter instalada a dep openpyxl
# %%
df.shape # mostra linhas e colunas do df

# %%
df.head() # Primeiras 5 linas do df

# %%
df.tail() # Últimas 5 linhas do df

# %%

colunas = ["UUID", "Points", "IdCustomer", "DtTransaction"]

df = df[colunas] # Reordenar colunas como desejar
df

# %%
df.info(memory_usage="deep")

# %%
