#Funções
#O que é?
#Uma função em programação é um bloco de código reutilizável que realiza uma tarefa específica. 
# Funções ajudam a modularizar o código, tornando-o mais organizado, reutilizável e fácil de entender. 
# Elas evitam a duplicação de código, permitindo que um trecho de código seja usado várias vezes em diferentes partes do programa.


#Parâmetros
#Os parâmetros são variáveis declaradas na definição da função. Eles são usados para receber valores quando a função é chamada. 
# Os parâmetros são colocados entre parênteses após o nome da função.

#Argumentos
#Os argumentos são os valores passados para a função quando ela é chamada. Eles correspondem aos parâmetros da função.

# def calcular_desconto(preco):
#     preco_final = preco * 0.8
#     return preco_final

# print(calcular_desconto(100))
valores = [100, 30, 45, 33, 99]

def mensagem():
    print("Olá, mundo!")



def calcular_desconto(preco):
    preco_final = preco * 0.8
    return preco_final

mensagem()
valor_desconto = calcular_desconto(100)

for valor in valores:
    print(f"O valor do desconto é de R$ {calcular_desconto(valor):.2f}")

###################################################


#Argumentos Arbritrários (*args e kwargs)
########################################
#Argumentos arbitrários com *args
def somar (*numeros):
    soma = sum(numeros)
    print(f"A soma dos números é {soma}")
somar(1, 2, 3, 4, 5)
######################################
#Argumentos arbitrários com **kwargs
def exibir_informacoes(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

exibir_informacoes(nome="João", idade=25, cidade="São Paulo")
#############################################################
#Retorno de múltiplos valores
def calcular(a,b):
    soma = a + b
    produto = a * b
    return soma, produto

s, p = calcular(5, 3)
print(f"A soma é {s} e o produto é {p}")
#############################################################
#Escopo local:

def funcao():
    x = 10
    print(x)

funcao()
print(x)
#############################################################
#Escopo global:
x = 20
def mostrar_valor():
    print(x)

mostrar_valor()
#############################################################
#Palavra Chave global:

contador = 0
def incrementar():
    global contador
    contador += 1
    print(contador)

incrementar()
print(contador)
#############################################################
#Função como argumento

def aplicar_operacao(funcao, valor):
    return funcao(valor)

def quadrado(x):
    return x ** 2

resultado = aplicar_operacao(quadrado, 5)
print(resultado)
#############################################################
#Função em recursão
#Recursão ocorre quando uma função chama a si mesma para resolver um problema. 
# É útil para resolver problemas que podem ser divididos em subproblemas menores, como calcular o fatorial de um número.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))






