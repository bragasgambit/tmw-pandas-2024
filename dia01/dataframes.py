import pandas as pd

# Dicionário da massa
data = {
    "nome": ["yuri", "ester", "paulo", "tania"],
    "sobrenome": ["braga", "trindade", "braga", "braga"],
    "idade": [25, 23, 28, 58],
}

print(data["idade"][0])

df = pd.DataFrame(data)
print("--")
print(df)  # Cada coluna do dataframe pode ser considado uma série
print("--")
# Acessar idade da primeira pessoa
print(df["idade"])  # isso é uma série

print(df["idade"].iloc[0])  # A série resolve o dataframe

print(df["sobrenome"].iloc[0])

print(df.iloc[0])  # Posso obter séries do df tanto com colunas quanto com linhas
# Lembrando: o 0 do iloc é posição. No output o Name: 0 é o índice
# df.iloc[] é a linha
# df[].iloc[] é a coluna

print("--")
print(df.index)
print(df.columns)
print(df.info())  # Não confie na Mem usage
print(df.info(memory_usage="deep"))  # Faça assim para saber a qtd de memória usada
print("--")

print(df.dtypes)  # Série que carrega as informaçÕes dos tipos de coluna

print(df.describe())  # aplica estatística para todas as var numéricas

# Adicionar coluna no df:
df["peso"] = [75, 70, 85, 65]

print(df)

sumario = (
    df.describe()
)  # tratar o df como uma planilha onde eu posso acessar como uma série:

print(
    "A media dos pesos adicionados posteriormente no DataFrame:",
    sumario["peso"]["mean"],
)

df.head()  # Mostra as 5 primeiras linhas do df ou .head(n)
df.tail()  # Mostras as 5 últimas linhas do df ou .tail(n)
