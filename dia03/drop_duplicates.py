# %%
import pandas as pd

data = {
    "Nome": ["Téo", "Nah", "Maria", "Nah", "Lara", "Téo"],
    "Idade": [32, 33, 2, 33, 31, 32],
    "updated_at": [1, 2, 3, 1, 2, 3],
}

df = pd.DataFrame(data)

# Removendo duplicatas
# df = df.drop_duplicates()
# A linha inteira precisa ser igual para remover

# Se quiser que remova uma duplicata com alguma coluna diferente basta passar o nome das colunas iguais utilizando subset=

# Uma boa forma de remover as duplicatas é organizando os valores (.sort_values) de (by=) updated_at em ordem descrescente (ascending=False) para os mais atuais ficarem primeiro
# Em seguida, remover as duplicatas (.drop_duplicates) utilizando as colunas desejadas como parâmetro (subset=) e mantendo (keep=) a primeira ocorrência da duplicata, que seria a mais atualizada

# %%
df = df.sort_values(by="updated_at", ascending=False).drop_duplicates(
    subset=["Nome", "Idade"], keep="first"
)

df
# %%
