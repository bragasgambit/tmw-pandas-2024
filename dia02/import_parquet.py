# %%
# Parquet é um tipo de objeto utilisado em engenharia de dados e big data com menor custo de armazenamento
# Formato .parquet é um binário utilizado para leitura e armazenamento de forma rápida que um .csv
# Tabela de 1 TB .csv pode chegar a 10 GB .parquet

import pandas as pd

df = pd.read_parquet("../data/transactions_cart.parquet")
df

# %%
