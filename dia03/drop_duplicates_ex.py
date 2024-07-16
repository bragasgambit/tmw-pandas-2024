# %%
# Retorne com a última transação de cada ID Customer

import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df
# %%
# Ordena para depois dropar (Ordem faz diferença)
df_last = df.sort_values(by=["DtTransaction"], ascending=[False]).drop_duplicates(
    subset="IdCustomer", keep="first"
)
df_last
# %%
# Como saber se deu certo???
# Usa o método nunique() para contar quantas linhas únicas tem:
df_last["IdCustomer"].nunique()
# Resulta em 727 que é o número de linhas que tem no df

# %%

df[df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"]

# %%
df_last[df_last["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"]
# df_last coincide com a última transação na base original df

# %%
