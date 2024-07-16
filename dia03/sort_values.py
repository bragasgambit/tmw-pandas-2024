# %%
# Ordenação de df's
import pandas as pd

# %%
df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%
# Ordenar o df por Points em ordem decrescente:
# Lembrando que para alterar o próprio df deve-se usar o rename ou o inplace=True
df.sort_values(by="Points", ascending=False, inplace=True)
df # Retorna um df ordenado

# %%
# Como fazer um "pipeline" (sequência de comandos) de dados renomeando os títulos?

# Ordena pela pontuação mais alta para a mais baixa e se houver empate o nome em ordem alfabética (crescente é o desempate)
df = df.sort_values(by=["Points", "Name"], ascending=[False, True]).rename(columns={"Name":"Nome", "Points":"Pontos"}
)

# inplace=True não funciona em um pipeline, por isso é melhor usar df = df.xxx
df

# %%
