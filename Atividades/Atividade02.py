
#Questão 01: Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.
"""
entrada = input("Digite os números separados por espaço: ")
numeros = entrada.split()
impares = []

for n in numeros:
    if int(n) % 2 != 0:
        impares.append(int(n))

print("Números ímpares:", impares)
"""

#Questão 02: Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.
"""
entrada = input("Digite os números separados por espaço: ")
numeros = entrada.split()
primos = []

for n in numeros:
    n = int(n)
    if n > 1:
        eh_primo = True
        for i in range(2, n):
            if n % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(n)

print("Números primos:", primos)
"""

#Questão 03: Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.
"""
entrada1 = input("Digite os valores da primeira lista separados por espaço: ")
lista1 = entrada1.split()

entrada2 = input("Digite os valores da segunda lista separados por espaço: ")
lista2 = entrada2.split()

lista1 = [int(x) for x in lista1]
lista2 = [int(x) for x in lista2]

resultado = []

for item in lista1:
    if item not in lista2:
        resultado.append(item)

for item in lista2:
    if item not in lista1:
        resultado.append(item)

print("Elementos únicos em apenas uma das listas:", resultado)

"""

#Questão 04: Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.
"""
entrada = input("Digite os números separados por espaço: ")
numeros = list(map(int, entrada.split()))
numeros_unicos = list(set(numeros))
numeros_ordenados = sorted(numeros_unicos)

if len(numeros_ordenados) < 2:
    print("Não há segundo maior número.")
else:
    print("O segundo maior número é:", numeros_ordenados[-2])
"""

#Questão 05: Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.
"""
pessoas = []

quantidade = int(input("Quantas pessoas você quer adicionar? "))

for i in range(quantidade):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    pessoas.append((nome, idade))

pessoas_ordenadas = sorted(pessoas)

print("\nLista ordenada por nome:")
for nome, idade in pessoas_ordenadas:
    print(f"{nome} - {idade} anos")
"""

#Questão 06: Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis?
""" 
Imagine que você tem uma lista de números, tipo as notas dos alunos de uma turma. Alguns valores podem estar muito diferentes
dos outros — esses são os outliers. 

Usando Desvio Padrão:
Calcule a média dos valores.
Calcule o desvio padrão (ele mostra o quanto os valores variam da média).
Considere como outliers os valores que estão muito longe da média, geralmente mais de 3 desvios padrão acima ou abaixo.

Exemplo: Se a média das notas é 70 e o desvio padrão é 10, então:
Valores abaixo de 70 - 3×10 = 40 ou acima de 70 + 3×10 = 100 são outliers.

Tratamento:
Você pode remover esses valores ou substituir por algo mais comum, como a média ou mediana.
#########################################################################################################################################
Usando Quartis (ótimo para dados com distribuição desigual):

Organize os dados em ordem.

Encontre o Q1 (25%) e o Q3 (75%) — são os quartis.

Calcule o IQR = Q3 - Q1.

Valores abaixo de Q1 - 1,5×IQR ou acima de Q3 + 1,5×IQR são outliers.

Exemplo: Se Q1 = 60 e Q3 = 80, então:

IQR = 80 - 60 = 20

Limites: abaixo de 60 - 30 = 30 ou acima de 80 + 30 = 110 são outliers.

Tratamento:

Mesmo esquema: remover, substituir ou analisar melhor se o valor faz sentido.

"""

#Questão 07: Como concatenar vários DataFrames (empilhando linhas ou colunas), mesmo que tenham colunas diferentes?
"""
Concatenar DataFrames é juntar dois ou mais DataFrames, seja empilhando linhas (um embaixo do outro) ou colando colunas (lado a lado).
Usando pd.concat():

Empilhar linhas (axis=0):
        import pandas as pd

        df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        df2 = pd.DataFrame({'B': [5, 6], 'C': [7, 8]})

        resultado = pd.concat([df1, df2], axis=0)

Junta os DataFrames verticalmente.

Como as colunas são diferentes, o pandas preenche com NaN onde não há dados.

Resultado terá colunas: A, B, C.
#########################################################################################################################################
Empilhar colunas (axis=1):

        resultado = pd.concat([df1, df2], axis=1)

Junta os DataFrames horizontalmente.

Se os índices não forem iguais, também haverá NaN.
#########################################################################################################################################
Ignorar os índices originais:

resultado = pd.concat([df1, df2], axis=0, ignore_index=True)
Cria um novo índice contínuo, útil quando você não quer manter os índices antigos.

Resumo prático:
Objetivo	                                Código	                                    Resultado
Empilhar linhas	                pd.concat([...], axis=0)	                          Um embaixo do outro
Empilhar colunas	            pd.concat([...], axis=1)	                          Lado a lado
Colunas diferentes	            pd.concat([...])	                                  Preenche com NaN
Ignorar índices	                pd.concat([...], ignore_index=True)	                  Índice novo e sequencial
"""

#Questao 08: Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?
"""
Para ler um CSV com pandas e exibir as primeiras linhas:

import pandas as pd

df = pd.read_csv('caminho/do/arquivo.csv') # Lê o arquivo CSV e cria um DataFrame

print(df.head()) # Exibe as primeiras 5 linhas do DataFrame

Explicando cada parte:
import pandas as pd: importa a biblioteca pandas.

pd.read_csv(...): lê o arquivo CSV e transforma em um DataFrame, que é como uma tabela.

'caminho/do/arquivo.csv': substitua pelo caminho real do seu arquivo. Ex: 'dados/alunos.csv'.

df.head(): mostra as primeiras 5 linhas do DataFrame. Se quiser mais ou menos, pode usar df.head(10) ou df.head(3).

Se o arquivo estiver com outro separador (como ponto e vírgula), use:

df = pd.read_csv('arquivo.csv', sep=';')
"""

#Questao 09: Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?
"""
Para Selecionar uma coluna específica utiliza:

df['Nome']
Isso retorna apenas os valores da coluna "Nome" do DataFrame df.

Para Filtrar linhas com base em uma condição utiliza:
O método .loc[] com uma condição lógica. Exemplo:

df_filtrado = df.loc[df['Idade'] > 25]
Isso seleciona apenas as linhas onde a coluna "Idade" tem valor maior que 25.

Exemplo:

import pandas as pd

# Criando um DataFrame de exemplo
df = pd.DataFrame({
    'Nome': ['Alice', 'Bob', 'Carlos', 'Diana'],
    'Idade': [24, 27, 22, 30]
})

# Selecionar a coluna 'Nome'
nomes = df['Nome']

# Filtrar linhas onde a idade é maior que 25
maiores_25 = df.loc[df['Idade'] > 25]

print(nomes)
print(maiores_25)

Dica extra:
Você pode combinar condições com & (E) ou | (OU):

df.loc[(df['Idade'] > 25) & (df['Nome'] == 'Diana')]
Isso seleciona quem tem mais de 25 anos e se chama Diana.
"""

#Questão 10: Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?
"""
Para identificar valores ausentes use:
.isna() ou .isnull() para ver onde estão os NaNs:

ndf.isna()      # Retorna True onde há NaN
df.isna().sum() # Conta quantos NaNs há por coluna

Para Remover valores ausentes
Se quiser excluir linhas ou colunas com NaN:

df.dropna()              # Remove linhas com qualquer NaN
df.dropna(axis=1)        # Remove colunas com qualquer NaN
df.dropna(thresh=2)      # Mantém linhas com pelo menos 2 valores não nulos

Preencher valores ausentes
Use .fillna() para substituir NaNs por algum valor:

df.fillna(0)             # Substitui NaNs por 0
df.fillna('Sem dado')    # Substitui por texto
df.fillna(df.mean())     # Preenche com a média da coluna (numérica)
Você também pode preencher com a mediana, moda, ou até com o valor anterior:

df.fillna(method='ffill')  # Preenche com o valor anterior (forward fill)
df.fillna(method='bfill')  # Preenche com o valor seguinte (backward fill)

Resumo:
Ação	                Código exemplo
Verificar NaNs	          df.isna()
Contar    NaNs	          df.isna().sum()
Remover linhas/colunas	  df.dropna()
Preencher com valor       df.fillna(0)
Preencher com média	      df.fillna(df.mean())
Preencher com anterior    df.fillna(method='ffill')

"""