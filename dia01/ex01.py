# Converta a seguinte lista de dados para uma Series Pandas e obtenha:
# Média
# Desvio Padrão
# Máximo Valor
import pandas as pd

dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]

s = pd.Series(dados, name="numbers")
print(f"Média: {s.mean()}")
print(f"Desvio Padrão: {s.std()}")
print(f"Valor Máximo: {s.max()}")
