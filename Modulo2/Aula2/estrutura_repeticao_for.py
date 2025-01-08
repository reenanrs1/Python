#damos um limite

# numero = int(input("Digite um número: "))

# print ("Tabuada do número", numero)

# for i in range(1,11):
#     print(numero, "x", i, "=", numero*i)
    
    
# frutas = ["maçã", "banana", "uva", "morango", "abacaxi"]

# for fruta in frutas:
#     print(fruta)

# palavra = "Python"

# for letra in palavra:
#     print(letra)

###LOOP CHAVE E VALOR
# aluno = {"nome": "João", "idade": 25, "nota": 9.5}

# for chave, valor in aluno.items():
#     print(f"{chave}:{valor}")


##Loop aninhados
# for i in range(3):
#     for j in range(2):
#         print(i,j)

matriz = [[1,2,3], [4,5,6], [7,8,9]]

for linha in matriz:
    for elemento in linha:
        print(elemento, end="-")
    print()
    
#USANDO BREAK
for i in range(10):
    if i == 5:
        break
    print(i)
for i in range(10):
    if i == 2:
        continue
print(i)

#  Utilizando condicionais de for
numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    if numero % 2 == 0:
        print(numero, "é par")
    else:
        print(numero, "é impar")
        