from colorama import Fore
import csv
import os
from datetime import datetime

def listar_eventos():
    try:
        with open("eventos.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)  # Pula o cabeçalho
            eventos = list(leitor)
            
            if not eventos:
                print(Fore.YELLOW + "Não há eventos cadastrados!")
                return True
                
            print(Fore.GREEN + "\nEventos disponíveis:")
            for evento in eventos:
                # Conta inscrições para este evento
                total_inscritos = 0
                try:
                    with open("inscricoes.csv", "r") as arquivo_inscricoes:
                        leitor_inscricoes = csv.reader(arquivo_inscricoes)
                        next(leitor_inscricoes)  # Pula o cabeçalho
                        for inscricao in leitor_inscricoes:
                            if inscricao[1].lower() == evento[0].lower():
                                total_inscritos += 1
                except FileNotFoundError:
                    pass
                
                vagas_restantes = int(evento[3]) - total_inscritos
                print(Fore.YELLOW + f"\nEvento: {evento[0]}")
                print(Fore.WHITE + f"Data: {evento[1]}")
                print(f"Descrição: {evento[2]}")
                print(f"Vagas restantes: {vagas_restantes}")
                
    except FileNotFoundError:
        print(Fore.RED + "Não há eventos cadastrados!")
    except Exception as e:
        print(Fore.RED + f"Erro ao listar eventos: {str(e)}")
        return False
    return True

def inscrever_evento():
    try:
        nome = input(Fore.GREEN + "Digite o seu nome: ").strip().lower()
        if not nome:
            print(Fore.RED + "O nome não pode estar vazio!")
            return False
            
        evento_desejado = input(Fore.GREEN + "Digite o evento que você deseja se inscrever: ").strip().lower()
        if not evento_desejado:
            print(Fore.RED + "O nome do evento não pode estar vazio!")
            return False
            
        # Verifica se o aluno já está inscrito no evento
        try:
            with open("inscricoes.csv", "r") as arquivo:
                leitor = csv.reader(arquivo)
                next(leitor)  # Pula o cabeçalho
                for inscricao in leitor:
                    if inscricao[0].lower() == nome.lower() and inscricao[1].lower() == evento_desejado.lower():
                        print(Fore.RED + "Você já está inscrito neste evento!")
                        return False
        except FileNotFoundError:
            pass

        # Verifica se o evento existe e tem vagas
        evento_encontrado = False
        with open("eventos.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)  # Pula o cabeçalho
            for evento in leitor:
                if evento[0] == evento_desejado:
                    evento_encontrado = True
                    vagas = int(evento[3])
                    
                    # Conta inscrições existentes
                    total_inscritos = 0
                    try:
                        with open("inscricoes.csv", "r") as arquivo_inscricoes:
                            leitor_inscricoes = csv.reader(arquivo_inscricoes)
                            next(leitor_inscricoes)  # Pula o cabeçalho
                            for inscricao in leitor_inscricoes:
                                if inscricao[1] == evento_desejado:
                                    total_inscritos += 1
                    except FileNotFoundError:
                        pass
                    
                    if total_inscritos >= vagas:
                        print(Fore.RED + "Desculpe, não há mais vagas disponíveis para este evento!")
                        return False
                    break
        
        if not evento_encontrado:
            print(Fore.RED + "Evento não encontrado!")
            return False
            
        # Cria ou adiciona ao arquivo de inscrições
        arquivo_existe = os.path.exists("inscricoes.csv")
        with open("inscricoes.csv", "a", newline='') as arquivo:
            escritor = csv.writer(arquivo)
            if not arquivo_existe:
                escritor.writerow(["Nome", "Evento", "Data_Inscricao"])
            escritor.writerow([nome, evento_desejado, datetime.now().strftime("%d/%m/%Y")])
            
        print(Fore.GREEN + "Inscrição realizada com sucesso!")
        return True
        
    except Exception as e:
        print(Fore.RED + f"Erro ao realizar inscrição: {str(e)}")
        return False

    
