#manipulando conjuntos - sets
#sets não tem  elementos duplicados e não são ordenados/não são indices

#o que são sets
#Um conjunto ou set é uma estrutura de dados que armazena uma coleção de elementos únicos e não ordenados. 
# Isso significa que os elementos de um conjunto não possuem duplicatas e não mantêm uma ordem específica. 
# Os conjuntos são frequentemente usados em operações que envolvem comparação e verificação de membros.

usuarios = {"renan", "maria", "joao", "pedro"}
usuarios.add("jose")
print(usuarios)

usuario_digitado = input("Digite o nome do usuario: ")

if usuario_digitado in usuarios:
    print(f"Usuario já existe")
else:
    usuarios.add(usuario_digitado)
    print(f"Usuario {usuario_digitado} adicionado com sucesso")
    print(usuarios)

novos_usuarios = {"carlos", "lucas", "renan"}

print(usuarios)
print(novos_usuarios)

uniao = usuarios.union(novos_usuarios)
print(f"União dos 2 tipos: {uniao}")

usuarios_comuns = usuarios.intersection(novos_usuarios)
print(f"Usuarios comuns: {usuarios_comuns}")

usuarios_diferentes = usuarios.difference(novos_usuarios)
print(f"Usuarios diferentes: {usuarios_diferentes}")

#Removendo Elementos com remove() e discard()
# O método remove() exclui um elemento do conjunto, mas gera um erro se o elemento não existir, enquanto discard() remove um elemento sem gerar erro se o elemento não estiver presente.

#Limpando e Excluindo Conjuntos
# •clear(): Remove todos os elementos do conjunto, deixando-o vazio.
# •del: Exclui o conjunto completamente.

#Looping em Conjuntos
# Os conjuntos podem ser percorridos usando loops, como o loop FOR, para acessar cada elemento individualmente.
# for elemento in conjunto_a:
#     print(elemento)

#Remoção de Duplicatas em Listas
# Os conjuntos são uma ferramenta eficaz para remover duplicatas de uma lista, convertendo a lista em um conjunto e retornando-a para uma lista.

# lista_com_duplicidade = [1,2,2,3,4,4,5]
#lista_unica = list(set(lista_com_duplicidade))
#print(lista_unica)

#Filtragem e Pesquisa Eficiente
# Devido à sua estrutura, conjuntos permitem verificações rápidas de existência de elementos, sendo muito eficientes em operações de busca.
# lista_com_duplicidade = [1,2,2,3,4,4,5]

