# Converta o seguinte dicionário para DataFrame e obtenha:
# Sumário de cada coluna
# Média da coluna idade
# Último nome da coluna nome
import pandas as pd

data = {"nome": ["Téo", "Nah", "Napoleão"], "idade": [31, 32, 14]}

df = pd.DataFrame(data)
print(df)

print("Sumério dos nomes:\n", df["nome"])  # Transforma o df em uma serie
print("Sumário das idades:\n", df["idade"])  # Transforma o df em uma serie

print("Média das idades:", df["idade"].mean())

print("Último nome da coluna nome:", df["nome"].iloc[-1])
# Poderia também ser df["nome"].tail(1)
