# %%

import pandas as pd

# Usado mais para frente
import numpy as np

# %%
df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%
# Executar um produto escalar aplica para todas as linhas
df["Points_double"] = df["Points"] * 2
df

# %%
# Operação aritmética de uma série com outra executa a operação em todas as linhas
df["Points_ratio"] = df["Points_double"] / df["Points"]
df
# Apereu NaN (Not a Number, aparece em int ou float) != "None"
# Na é guarda-chuva (contém Na, None, NaN)

# %%

df["Constante"] = None
df

# %%
# Criar uma coluna ["Points_log"] e aplica o log utilizando a biblioteca numpy(np)
df["Points_log"] = np.log(df["Points"])
df

# %%
# Aplicou o logo nas 3 colunas
np.log(df[["Points", "Points_double", "Points_ratio"]])

# %%
# Colocar todos os elementos de uma coluna em caixa alta:
nomes_alta = []
for i in df["Name"]:
    nomes_alta.append(i.upper())

df["Nome_Alta"] = nomes_alta
df
# ISSO NÃO É BOM POR USAR O FOR QUE PERCORRE O DF INTEIRO UM POR UM
# Melhor usar uma aplicação vetorial

# %%
# Aqui: Pega a série, atribui a ela uma string e usa o método upper()
df["Name"].str.upper()

# Infinitamente melhor que usar for

# %%
# Forma de pensar: "o que eu quero fazer com cada elemento?" Escreva uma função sempre pensando no elemento
# Definir uma função personalizada que fique apenas com o nome antes da primeira _
# eg Antonio_Carlos  ->  Antonio

def get_first(nome: str):
    nome = nome.upper()
    return nome.split("_")[0]
# No nome divide (.split) quando aparecer "_" em uma lista e apresenta apenas o primeiro item da série

# %%
# .apply(<funct>)  -  aplica uma função em todas as linhas da série
# A função no python também é um objeto, então pode ser usada em um método
df["Name_First"] = df["Name"].apply(get_first)
df

# %%
# lambda é uma função simples que não precisa ser rigorosamente definida
# soma = lambda x, y: x + y
# no lugar da função get_first definida com def, pode passar uma função lambda

df["Name"].apply(lambda x: x.upper().split("_")[0])
# Essa é a forma mais utilizada

# %%
# Faixas de pontuação adicionando no df:

def intervalo_pontos(pontos):
    if pontos < 2500:
        return "baixo"
    elif pontos < 3500:
        return "medio"
    else:
        return "alto"


df["Faixa_Pontos"] = df["Points"].apply(intervalo_pontos)
df
# Nesse caso não dá para usar lambda por ser uma estrutura com if else

# %%
# Criar uma coluna com os 3 últimos caracteres da UUID
df["UUID"].apply(lambda x: x[-3:])
# A série df["UUID"] vai ser aplicada a função que remove os 3 últimos [-3:] caracteres de cada UUID

# %%
# Tudo está sendo aplicado em uma série
# Uma série tem elementos e estou aplicando em todos os elementos
# E como aplicar no df?
df

# %%
# "Motivo pelo qual o ifood manda cupom de desconto quando você não está comprando"
# crm := Customer Relationship Management - Forma de medir a relação do cliente com o produto de forma estatística
# A forma de medir o CRM é com o RFV := Recency, Frequency, Value
# Recency (Recência) é o tempo desde a última compra
# Frequency é a frequência que pagou pelo serviço em um tempo x
# Value é a soma de valores gastos em um tempo x

data = {
    "nome": ["Teo", "Nah", "Maria", "Lara"],
    "recencia": [1, 30, 10, 45], # Tempo que está sem comprar no ifood
    "valor": [100, 2000, 15, 500],
    "frequencia": [2, 5, 1, 15],
}

df_crm = pd.DataFrame(data)

# Se recencia <= 10:
    # Ganha nota 10
# Se recencia > 10 e < 30:
    # Ganha nota 5
# Se recencia > 30:
    # Ganha nota 0

# Se valor > 1000:
    # Nota 10
# Se valor < 100 e > 1000:
    # Nota 5
# Se valor < 1000:
    # Nota 0

# Se frequencia > 10:
    # Nota 10
# Se frequencia < 10 e > 5:
    # Nota 5
# Se frequencia < 5:
    # Nota 0

# Nota_final = somatorio_notas

def rfv(row):
    nota = 0

    if row["recencia"] <= 10:
        nota += 10
    elif 10 < row["recencia"] <= 30:
        nota += 5
    elif row["recencia"] > 30:
        nota += 0

    if row["valor"] > 1000:
        nota += 10
    elif 100 <= row["valor"] < 1000:
        nota += 5
    elif row["valor"] < 100:
        nota += 0

    if row["frequencia"] > 10:
        nota += 10
    elif 5 <= row["frequencia"] < 10:
        nota += 5
    elif row["frequencia"] < 5:
        nota += 0

    return nota

# No final, a função está sendo definida utilizando uma linha (row) do df_crm e agora estou pegando o índice (eg row["valor"])

# row é a linha do df
# column é a coluna do df

# %%
# Vou criar uma nova coluna RFV no df_crm de forma que no df_crm original é aplicado (apply) a função (rfv), mas é preciso especificar que estou passando uma linha por vez (axis=1)
# Lembrando: .apply retorna uma série
# rfv está recebendo a linha inteira do df_crm

df_crm["RFV"] = df_crm.apply(rfv, axis=1)
df_crm

# Portanto, o cliente mais valioso é a Nah, seguido da Lara, Teo e Maria

# %%
# O rfv é o que o iloc faz, percorre a linha
df_crm.iloc[0]
# Retorna uma série com todos os elementos da linha

# %%
