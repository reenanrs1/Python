numero = int(input("Digite um número: "))

contador = 0
#Função dele é repitir o bloco de código enquanto a condição for verdadeira
while contador <= numero:
    print(contador)
    contador += 1
    
numero = int(input("Digite um número para a tabuada: "))
limite = int(input("Digite o limite da tabuada: "))
contador = int(input("Digite o contador da tabuada: "))

while contador <= limite:
    resultado = numero * contador
    print(f"{numero} x {limite} = {resultado}")
    contador += 1