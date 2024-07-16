# %%
import pandas as pd

df = pd.read_csv(
    "../data/products.csv",
    sep=";",
    # header=None,
    names=["ID", "Name", "Description"],
)
df
# No arquivo não tem cabeçalho, portanto deve ser utilizado o header para utilizar um cabeçalho sem nada de informação. Usar names se quiser passar os nomes em forma de lista []

# %%

df = df.rename(
    columns={"Name": "Nome", "Description": "Descrição"}
)  # Não precisa reatribuir, apenas passar o inplace=True
df

# %%
