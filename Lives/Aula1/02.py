# um vendedor recebe uma comissão por suas vendas
# dependendo do valor da venda, a comissão varia
# A comissão é calculada da seguinte forma:
#     - 5% para vendas de até 1000 reais
#     - 7,5% para vendas de 1001 a 5000 reais
#     - 10% para vendas acima de 5001 e 10.000 reais
#     - 15% para vendas acima de 10.000
# escreva um programa em python que calcule andcomissão do vendedor dado o valor da venda e o nome do vendedor

nome_vendedor = input("Digite o nome do vendedor: ")
valor_venda = float(input("Digite o valor da venda: "))

if valor_venda <= 1000:
    comissao = valor_venda * 0.05
elif valor_venda >= 1001 and valor_venda <= 5000:
    comissao = valor_venda * 0.075
elif valor_venda >= 5001 and valor_venda <= 10000:
    comissao = valor_venda * 0.10
else:
    comissao = valor_venda * 0.15

print(f"O vendedor {nome_vendedor} recebeu uma comissão de R$ {comissao:.2f}, totalizando o ganho de R$ {valor_venda + comissao:.2f}")