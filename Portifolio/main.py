from colorama import init, Fore
from datetime import datetime, date
import os
import csv
import coordenador
import aluno

init(autoreset=True)

#Limpar tela
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
    
#Pausar
def pausar():
    input(Fore.BLUE + "Pressione Enter para continuar...")
    
#Menu sistema
def menu_sistema(opcao):
    opcao = opcao.strip().lower()  # Normaliza a entrada
    
    if 'coordenador' in opcao or 'cordenador' in opcao: 
        print(Fore.GREEN + '1 => Cadastrar eventos')
        print(Fore.GREEN + '2 => Atualizar eventos')
        print(Fore.GREEN + '3 => Visualizar Inscrições')    
        print(Fore.GREEN + '4 => Exluir Evento')
        print(Fore.GREEN + '5 => Listar eventos disponiveis')
        print(Fore.GREEN + '6 => Sair')
    elif 'aluno' in opcao:
        print(Fore.GREEN + '1 => Listar eventos disponiveis')
        print(Fore.GREEN + '2 => Inscrever em um evento')
        print(Fore.GREEN + '3 => Sair')
    else:
        print(Fore.RED + 'Opção inválida')
 
#Processar opção
def processar_opcao(opcao, tipo_usuario):
    tipo_usuario = tipo_usuario.strip().lower()
    resultado = False
    
    # Validar opção antes de processar
    if 'coordenador' in tipo_usuario or 'cordenador' in tipo_usuario:
        if opcao not in ['1', '2', '3', '4', '5', '6']:
            print(Fore.RED + 'Opção inválida!')
            pausar()
            return
    elif 'aluno' in tipo_usuario:
        if opcao not in ['1', '2', '3']:
            print(Fore.RED + 'Opção inválida!')
            pausar()
            return

    try:
        if 'coordenador' in tipo_usuario or 'cordenador' in tipo_usuario:
            if opcao == '1':
                resultado = coordenador.cadastrar_evento()
            elif opcao == '2':
                resultado = coordenador.atualizar_evento()
            elif opcao == '3':
                resultado = coordenador.visualizar_inscricoes()
            elif opcao == '4':
                resultado = coordenador.excluir_evento()
            elif opcao == '5':
                resultado = coordenador.listar_eventos()
        elif 'aluno' in tipo_usuario:
            if opcao == '1':
                resultado = aluno.listar_eventos()
            elif opcao == '2':
                resultado = aluno.inscrever_evento()
    except Exception as e:
        print(Fore.RED + f"Erro inesperado: {str(e)}")
        resultado = False
    
    if resultado is not None:
        pausar()
    return

def sistema():
    while True:
        try:
            limpar_tela()
            tipo_usuario = input(Fore.GREEN + 'Digite se você é Coordenador ou Aluno: ').strip()
            tipo_usuario_lower = tipo_usuario.lower()
            
            if not ('coordenador' in tipo_usuario_lower or 
                    'cordenador' in tipo_usuario_lower or 
                    'aluno' in tipo_usuario_lower):
                print(Fore.RED + 'Tipo de usuário inválido! Digite "Coordenador" ou "Aluno"')
                pausar()
                continue
            
            limpar_tela()
            menu_sistema(tipo_usuario)
            opcao = input(Fore.YELLOW + "Digite a opção desejada: ").strip()
            limpar_tela()
            
            if (('coordenador' in tipo_usuario_lower or 'cordenador' in tipo_usuario_lower) and opcao == '6') or \
               ('aluno' in tipo_usuario_lower and opcao == '3'):
                print(Fore.GREEN + "Saindo do sistema...")
                pausar()
                break
                
            processar_opcao(opcao, tipo_usuario)
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\nOperação cancelada pelo usuário.")
            pausar()
            break
        except Exception as e:
            print(Fore.RED + f"Erro inesperado: {str(e)}")
            pausar()
            continue

sistema()