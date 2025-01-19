from colorama import init, Fore
import os
import csv
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
        cidade = input(Fore.GREEN + "Digite o nome da cidade: ")
        estado = input(Fore.GREEN + "Digite o nome do estado: ")
        # Verifica se o arquivo existe
        arquivo_existe = os.path.exists("Modulo4/Projeto/cidades.csv")
        # Se o arquivo não existe, cria com cabeçalho
        # Se existe, verifica se está vazio
        arquivo_vazio = arquivo_existe and os.path.getsize("Modulo4/Projeto/cidades.csv") == 0
        
        with open("Modulo4/Projeto/cidades.csv", "a", newline='') as arquivo:
            escritor = csv.writer(arquivo)
            if not arquivo_existe or arquivo_vazio:
                escritor.writerow(["cidade", "estado"])
            escritor.writerow([cidade, estado])
            
    elif opcao == "3":
        cidade = input(Fore.GREEN + "Digite o nome da cidade: ")
        encontrada = False
        with open("Modulo4/Projeto/cidades.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)  # Pula o cabeçalho
            for linha in leitor:
                if cidade.lower() in linha[0].lower():
                    print(f'{Fore.GREEN}Cidade encontrada: {linha[0]} - {linha[1]}')
                    encontrada = True
                    break
            if not encontrada:
                print(Fore.RED + "Cidade não encontrada")
                    
    elif opcao == "4":
        cidade = input(Fore.GREEN + "Digite o nome da cidade: ")
        
            
            
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