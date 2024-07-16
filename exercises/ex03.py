# Carregue os dados do arquivo data/ipea/homicidios.csv de forma correta e informe:
# Quantidade de linhas
# Quantidade de colunas
# Nome da primeira coluna
# Nome da última coluna
# %%
import pandas as pd

df = pd.read_csv("../data/ipea/homicidios.csv", sep=";")
df

# %%
# .shape imprime a dimensionalidade do df

df.shape[0]
# 891 linhas
# %%
df.shape[-1]
# 4 colunas
# %%
# Nome da primeira coluna
df.columns[0]

# %%
# Nome da última coluna
df.columns[-1]

# %%
