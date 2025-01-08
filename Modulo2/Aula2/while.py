#O WHILE é uma estrutura de repetição que executa um bloco de código repetidamente enquanto uma condição específica for verdadeira. 
# Em outras palavras, enquanto a condição for avaliada como True, o loop continua. O WHILE é muito útil em situações onde não se sabe 
# previamente quantas vezes o bloco de código será repetido, mas o loop depende de uma condição dinâmica.


#Como Funciona? Resposta
#O loop WHILE funciona de maneira simples: ele verifica a condição antes de cada iteração. 
# Se a condição for verdadeira, o bloco de código dentro do loop é executado. Após a execução do bloco de código, 
# a condição é verificada novamente, e isso se repete até que a condição se torne falsa. Quando a condição for falsa, o 
# loop é interrompido e o programa continua com as próximas instruções após o loop.

# Exemplo de uso do WHILE
############################################################################################################
# senha = input("Digite a senha: ")
# senha_correta = "python"


# while senha != senha_correta:
#     senha = input("Senha inválida. Digite novamente: ")
    
# print("Acesso permitido")

############################################################################################################
# contador = 1

# while contador <= 5:
#     print(contador)
#     contador += 1
############################################################################################################
#Contagem Regressiva
# Vamos usar o loop WHILE para criar uma contagem regressiva de 10 até 1:
# Aqui, o loop imprime o valor do contador enquanto ele for maior que 0. Quando o contador chega a 0, o loop é encerrado, e a mensagem "Contagem finalizada!" é exibida.

# contador = 10

# while contador > 0:
#     print(contador)
#     contador -= 1
# print("Fim do loop")
############################################################################################################

#Exemplo com Condicional:
#Neste exemplo, o loop WHILE verifica se o número é par ou ímpar em cada iteração e imprime a mensagem correspondente.
# num = 5
# while num > 0:
#     if num % 2 == 0:
#         print(num, "é par")
#     else:
#         print(num, "é impar")
#     num -= 1
############################################################################################################
# Exemplo com break:
# Aqui, o loop WHILE seria infinito sem o break, mas a instrução break é usada para parar o loop quando o contador atinge 6.

# contador = 1
# while True:
#     print(contador)
#     contador += 1
#     if contador > 5:
#         break
############################################################################################################
# Exemplo com continue:
# Neste exemplo, o valor 3 não será impresso, pois a instrução continue faz com que o loop pule diretamente para a próxima iteração quando contador for igual a 3.

# contador = 0

# while contador < 5:
#     contador += 1
#     if contador == 3:
#         continue
#     print(contador)
############################################################################################################
# Exemplo de WHILE Aninhado:
# Aqui, o loop externo (com i) é executado três vezes, e para cada valor de i, o loop interno (com j) é executado duas vezes, resultando em múltiplas combinações de valores para i e j.

# i = 1
# while i <= 3:
#     j = 1
#     while j <= 2:
#         print(f"i = {i}, j = {j}")
#         j += 1
#     i += 1
    
############################################################################################################
# Exemplo com Entrada de Usuário:
# Neste exemplo, o loop continuará pedindo a entrada do usuário até que ele digite "sair", momento em que o loop será encerrado.

# entrada = ""

# while entrada != "sair":
#     entrada = input("Digite 'sair' para encerrar o loop: ")
#     print(f"Você digitou: {entrada}")
    
############################################################################################################

# Exemplo de Função com WHILE:
# Neste exemplo, a função dobro() é chamada dentro do loop WHILE para calcular e imprimir o dobro de cada número.

# def dobro(n):
#     return n*2

# num = 1

# while num <= 5:
#     print(f"Dobro de {num} é {dobro(num)}")
#     num += 1

############################################################################################################
# Erros que ocorrem Exemplo de Loop Infinito:
# Neste exemplo, o loop nunca termina porque a condição contador > 0 é sempre verdadeira.

# contador = 1
# while contador > 0:
#     print(contador)

############################################################################################################

#Neste caso, o loop FOR executa exatamente 5 vezes, pois o intervalo de valores é definido pelo range(5).
for i in range(5):
    print(i)

#Aqui, o loop WHILE continua a iterar enquanto a condição contador < 5 for verdadeira. As iterações param quando contador atinge o valor 5.
contador = 0
while contador < 5:
    print(contador)
    contador += 1
