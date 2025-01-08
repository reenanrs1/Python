#O que são estruturas de dados?
#As estruturas de dados são maneiras organizadas de armazenar e manipular informações em um programa de forma eficiente. 
# Elas fornecem uma forma de organizar dados para que possam ser acessados e processados rapidamente. Estruturas como listas, 
# pilhas, filas e dicionários são fundamentais para resolver problemas complexos de maneira organizada.



#Manipulando listas - listas

nomes = ['Ana', 'Maria', 'José', 'Pedro', 'Elena', 'Helena', 'Elen']

print(f"Lista original: {nomes}")

#Adicionando 3 nomes na lista
for cont in range(3):
    novo_nome = input("Digite um novo nome: ")
    nomes.append(novo_nome)
print(f"Lista que houve input{nomes}")

#Adicionando nomes na lista enquanto o usuário desejar
resp = "sim"
while resp =="sim":
    novo_nome = input("Digite um novo nome: ")
    nomes.append(novo_nome)
    resp = input("Deseja adicionar mais um nome? sim ou não: ")
print(f"Lista que houve input{nomes}")

#Listando elementos pela sua posição.
print(f"O primeiro nome da lista é: {nomes[0]}")

#Removendo o último elemento da Lista
nomes.pop()
print(f"Lista após remover o último elemento: {nomes}")

#Removendo um elemento específico da lista
nome_remover = input("Digite o nome que deseja remover: ")
nomes.remove(nome_remover)
print(f"Lista após remover o nome {nome_remover}: {nomes}")

#Verificando a existencia de um elemento.
nome_pesquisar = input("Digite o nome que deseja pesquisar: ")
if nome_pesquisar in nomes:
    print(f"O nome {nome_pesquisar} está na lista.")
else:
    print(f"O nome {nome_pesquisar} não está na lista.")
    
#Usando o insert você pode adicionar um elemento em uma posição específica da lista exemplo primeiro indice, segundo indice, e o nome que deseja adicionar.
# nomes.insert(0, "Fernando")
tamanho = len(nomes)
print(tamanho) #Informa quantos elementos tem na lista
sorted(nomes) #Ordena a lista ou numeos = [5, 2, 3, 1, 4] numeros.sort() print(numeros) #Ordena a lista em ordem cresecente/usando reverse ele ordena em ordem decrescente

#Uso de max() e min()

# Essas funções retornam, respectivamente, o maior e o menor valor em uma lista de números.
# Exemplo: numeros = [5, 2, 3, 1, 4] print(max(numeros)) # Saída: 5 print(min(numeros)) # Saída: 1

#Exemplo de iterar sobre uma lista com for
frutas = ['maçã', 'banana', 'uva', 'morango', 'abacaxi']
for fruta in frutas:
    print(fruta)

##Iterando com Enumerate
# A função enumerate() é útil para obter tanto o índice quanto o valor de cada item durante a iteração.

for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

#Lista multidimensional
# Uma lista multidimensional é uma lista que contém outras listas.
# Exemplo: lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] print(lista[0]) # Saída: [1, 2, 3] print(lista[1][0]) # Saída: 4

#LiST COMPREHENSION
# List comprehension é uma maneira concisa de criar listas.
quadrados = [ x**2 for x in range(10) ]
print(quadrados) # Saída: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#explique para mim o que é o x**2 e o range(10) e o que ele faz.
#O x**2 é uma expressão que calcula o quadrado de x, e o range(10) cria uma lista de números de 0 a 9.