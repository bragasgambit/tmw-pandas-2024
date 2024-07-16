# %%
import pandas as pd

df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%

df.dtypes
# Retorna uma série
# Caso eu queira converter Points (int64) para string, basta:
# df["Points"].astype(str)

# %%
# Adicionei uma coluna na lista
df["Points_double"] = df["Points"] * 2

# %%
# Mudei o tipo das colunas Points e Points_double para float
df[["Points", "Points_double"]].astype(float)

# %%
# Não dá para converter uma str para um int:
# df[["UUID", "Name"]].astype(int)
# Não vai dar certo o output

# %%
# Adicionei uma coluna onde cada linha tem a lista [1, 2]
df["Lista"] = [[1, 2] for i in df.index]
df

# %%

df.dtypes

# %%
