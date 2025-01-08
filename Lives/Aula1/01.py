##Uma empore quer calcular o salário dos seus
#funcionários com base em sua carga horária
# semana e o valor da hora de trabalho
# alem disso, a empresa oferece um bonus
# de 10% para aqueles funcionários 
# que trabalharem mais de 40 horas por semana

carga_horaria = int(input("Digite a carga horária semanal: "))
valor_hora = float(input("Digite o valor da hora de trabalho: "))

salario = carga_horaria * valor_hora

if carga_horaria > 40:
    salario = salario * 1.10
else:
    salario = salario
print(f"O salário do funcionário é R${salario:.2f}")