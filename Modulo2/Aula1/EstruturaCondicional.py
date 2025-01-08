horas = input('Digites as horas trabalhadas: ')
valor = input('Digite o valor da hora: ')

if horas >= 100:
    salario = (horas * valor) + 500
else:
    salario = horas * valor
    
print('O salário é: ', salario)