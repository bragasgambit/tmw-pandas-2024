# .csv é um arquivo de texto que é separado por algum caractere especial onde cada linha é um registro
# para um exemplo ver o arquivo products.csv

import pandas as pd

df_customers = pd.read_csv("../data/customers.csv", sep=";") # Mudar o sepador, pois o padrão é ","

df_customers.shape # quantidade de linhas e colunas



df_customers.info(memory_usage="deep") # quantidade de memória


df_customers["Points"].describe() # Estatística descritiva da quantidade de pontos
# Veja que a mediana (50%) é 58 pts e a média é 206. Isso indica que a distribuição de pontos é bastante assimétrica (poucos tem muito e muitos tem pouco)
# Média é muito influenciada pelos outliers

# Como eu posso pegar o maior valor do df_customers??
# Vejamos como uma lista se comporta:

# Em uma lista, quero pegar todas as notas maiores que 5:
notas = [4.5, 6, 7, 3.5]
print(notas)

for i in notas:
    if i > 5:
        print(i)

# Somar um em todas as notas:
notas_novas = []
for i in notas:
    notas_novas.append(i + 1)

print(notas_novas)

# Em séries pode fazer operações escalares e vetoriais
print(df_customers["Points"] + 1000) # Pega o vetor e soma com um escalar (+  -  *  /  ...)

true_1000 = df_customers["Points"] > 1000 # Operação que retorna uma série do tipo boolean

# Forma de fazer filtro em pandas (True/False)
df_customers[true_1000] # Retorna apenas as linhas True
print(df_customers[true_1000])

###################################
# Retornando à pergunta da linha 19:
max_pts = df_customers["Points"].max() # Esse é só a quantidade max de pontos
print(max_pts)

condicao_max = df_customers["Points"] == max_pts # Retorna uma serie boolean com tudo False exceto a linha com o valor máximo
df_customers[condicao_max]

##################################
# O mais comum é fazer mais direto:
condicao = df_customers["Points"] == df_customers["Points"].max()
df_customers[condicao]
# Em apenas duas linhas consigo obter o que desejo: "Quem é o user que tem mais pontos"... Mas isso pode ser feito em uma linha...

#################################
# Aplicação de filtro em df's:
df_customers[df_customers["Points"] == df_customers["Points"].max()]
# Aplicar o filtro True para a série boolean de Points maximos
#################################

# Agora posso aplicar o filtro ["Names"] e saber só o nome direto:
print(df_customers[df_customers["Points"] == df_customers["Points"].max()]["Name"]) # Série com uma posição apenas

# Portanto: use .iloc na pos 0
print(df_customers[df_customers["Points"] == df_customers["Points"].max()]["Name"].iloc[0])


# Agora quero saber quem está entre 1000 e 2000
## Serão duas condições lógicas: (bool1) & (bool2)
print(df_customers[(df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)])

# Existe apenas uma lista
a = [1, 2, 3, 4]
b = a
print(a)
print(b)
# No python tudo e referência, cada elemento da lista é apenas uma referência para um objeto
b.append(5)
print(a)
print(b) # b é o mesmo objeto de a
# a = b, portanto só existe uma lista e não duas
# Só existe uma geladeira na sua casa, se altera a temperatura dela, todas as pessoas da casa (a, b, c, d) usam a mesma geladeira com a temperatura alterada!
# Da mesma forma um dataframe não cria outro dataframe quando faz uma consulta/filtragem, ele apenas mostra a referência no próprio dataframe.

# Se você aplica um filtro para depois manipular o dado, faça uma cópia antes de manipulá-lo!!!

# Agora são duas geladeiras:
b = a.copy() # cria um novo objeto
b.append(10)

print(a)
print(b) # b agora é uma cópia que pode ser modificada independente de a
