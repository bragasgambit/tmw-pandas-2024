import pandas as pd


idades = [30, 42, 90, 34]
idades

media = sum(idades) / len(idades)
print(media)
# Calcular desvio padrão é uma soma onde eu subtraio cada elemento da média e divido pelo número de elementos - 1 elevando ao quadrado
total = 0
for i in idades:  # Percorrer todas as idades
    total += (
        (media - i) ** 2
    )  # Pega a média (valor fixo) e subtrai da idade em específico com a iteração, eleva ao quadrado e soma no total

variancia = total / (len(idades) - 1)

print(variancia)
# puta trampo

# Mediana: ordena, calcula a posição do meio, se for par é uma coisa se for ímpar é outra coisa... Chato de trabalhar com manipulação de dados. Vamos usar Pandas :)

series_idades = pd.Series(
    idades, name="idades"
)  # Converte uma lista em uma série e atribuindo em uma var nova (ie series_idades)
# Se quiser dar o nome só depois basta usar o .name = "nome desejado" --funciona como em uma célula do excel

print(series_idades)

print(series_idades.mean())
print(series_idades.var())
print(series_idades.median())
print(series_idades.std())
print(series_idades.quantile(0.75))

print(series_idades.describe())

print(series_idades.shape)  # tuple

idades[0]  # List index
series_idades[0]  # Series index

print(series_idades.index)  # Starts in 0, stop in 4, step in 1
series_idades.index = ["t", "e", "o", "c"]  # Didática, não se faz isso

print(series_idades.index)
# Agora tem o índice, mas pode acessar pela posição ainda "range(4)"
print(series_idades["t"])
# print(series_idades[0]) poor way to navigate via position. Instead use the index

series_idades.iloc[
    0
]  # Quando o interesse é só na posição usa o .iloc[] --funciona como lista

series_idades.index = ["1", "2", "3", "4"]
