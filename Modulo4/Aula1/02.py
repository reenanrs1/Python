import random
import operacoes
from colorama import Fore, Style

def menu():
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Número aleatório")
    print("6. Sair")
    
def obter_valores():
    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))
    return a, b

while True:
    opção = menu()
    opção = int(input("Digite a opção desejada: "))
    if  opção == 6:
        print("Saindo...")
        break

    
    if opção == 1:
        a, b = obter_valores()
        print(f"{Fore.YELLOW}Resultado: {operacoes.soma(a,b)}{Style.RESET_ALL}")
    elif opção == 2:
        a, b = obter_valores()
        print(f"{Fore.YELLOW}Resultado: {operacoes.subtração(a,b)}{Style.RESET_ALL}")
    elif opção == 3:
        a, b = obter_valores()
        print(f"{Fore.YELLOW}Resultado: {operacoes.multiplicação(a,b)}{Style.RESET_ALL}")
    elif opção == 4:
        a, b = obter_valores()
        if b != 0:
            print(f"{Fore.YELLOW}Resultado: {operacoes.divisão(a,b)}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Não é possível dividir por zero{Style.RESET_ALL}")
    elif opção == 5:
        a, b = obter_valores()
        resultado = random.randint(a,b)
        print( f"{Fore.GREEN}Número aleatório: {resultado}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Opção inválida{Style.RESET_ALL}")
    
