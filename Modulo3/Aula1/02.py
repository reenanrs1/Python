#Manipulando tuplas - tuplas são imutáveis
#O que é uma tupla?
#Uma tupla é uma estrutura de dados imutável que armazena uma 
# coleção ordenada de elementos. Diferente das listas, uma vez que uma tupla é criada, 
# seus valores não podem ser modificados. As tuplas são frequentemente usadas quando é 
# necessário garantir que os dados permaneçam constantes ao longo da execução do programa.


cores = ('verde', 'amarelo', 'azul', 'branco')
print(cores)

qtd = len(cores)
print(f"Tenho {qtd} cores")

cor = input("Digite uma cor: ")

if cor in cores:
    qtd_cor = cores.count(cor)
    print(f"Temos {qtd_cor} tipo de {cor}")
else:
    print(f"A cor {cor} não existe na loja")
    
aluno = ("Renan", 10, 5)

#2 metodos de desempacotamento
# nome = aluno[0]
# nota1 = aluno[1]
# nota2 = aluno[2]
nome, nota1, nota2 = aluno
#media = (nota1 + nota2) / 2
print(f"O aluno {nome} tirou {nota1} e {nota2} e está com média {((nota1 + nota2) / 2)}")

#uso de funções
def coordenadas():
    return (10, 20)

x, y = coordenadas()
print(f"X: {x} e Y: {y}")