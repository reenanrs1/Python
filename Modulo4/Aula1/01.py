#Funções

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
