# Carregue os dados do arquivo data/ipea/homicidios-mulheres-negras.csv de forma correta e informe:
# Quais colunas são do tipo numérico?
# Quantas colunas são do tipo ‘object’?
# Qual o tamanho destes dados em memória?
# %%
import pandas as pd

df = pd.read_csv("../data/ipea/homicidios-mulheres-negras.csv",sep=";")
df
# %%
# Quais colunas são do tipo numérico?
df.columns[df.dtypes == "int64"]
# Escolhi filtrar pelas colunas que são int64 (a filtragem gera um bool True) e mostrar no output essas colunas

# %%
# Quantas colunas são do tipo ‘object’?
len(df.columns[df.dtypes == "object"])

# %%
# Qual o tamanho destes dados em memória?
df.info(memory_usage="deep")

# %%
