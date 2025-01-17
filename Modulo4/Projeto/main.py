from colorama import init, Fore
import os
from cidades import ler_cidades

init(autoreset=True)

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
def pausar():
    input(Fore.BLUE + "Pressione Enter para continuar...")
    
def exibir_menu():
    print(Fore.GREEN + "====MENU====")
    print(Fore.GREEN + "1. Listar cidades")
    print(Fore.GREEN + "2. Adicionar cidade")
    print(Fore.GREEN + "3. Buscar cidade")
    print(Fore.GREEN + "4. Atualizar cidade")
    print(Fore.GREEN + "5. Excluir cidade")
    print(Fore.GREEN + "6. Sair")
    
def processar_opcao(opcao):
    if opcao == "1":
        cidades = ler_cidades()
        for cidade in cidades:
            print(f"{Fore.GREEN}{cidade}")
    elif opcao == "2":
        return
    elif opcao == "3":
        return
    elif opcao == "4":
        return
    elif opcao == "5":
        return
    elif opcao == "6":
        print(Fore.GREEN + "Saindo do sistema...")
        exit()
    else:
        print(Fore.RED + "Opção inválida")
        
def executar_sistema():
    exibir_menu()
    
    opcao = input("Digite a opção desejada: ")
    
    limpar_tela()
    
    processar_opcao(opcao)
    
    pausar()
    
    executar_sistema()
    
executar_sistema()