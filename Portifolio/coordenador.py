from colorama import Fore
from datetime import datetime
import csv


def cadastrar_evento():
    try:
        evento = input(Fore.GREEN + "Digite o nome do evento: ").strip().lower()
        if not evento:
            print(Fore.RED + "O nome do evento não pode estar vazio!")
            return False
            
        data_str = input(Fore.GREEN + "Digite a data do evento (dd/mm/aaaa): ").strip()
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y").date()
            if data < datetime.now().date():
                print(Fore.RED + "A data do evento não pode ser no passado!")
                return False
        except ValueError:
            print(Fore.RED + "Formato de data inválido! Use dd/mm/aaaa")
            return False
            
        descricao = input(Fore.GREEN + "Digite a descrição do evento: ").strip()
        if not descricao:
            print(Fore.RED + "A descrição não pode estar vazia!")
            return False
            
        try:
            numero_maximo_participantes = int(input(Fore.GREEN + "Digite o numero maximo de participantes: "))
            if numero_maximo_participantes <= 0:
                print(Fore.RED + "O número máximo de participantes deve ser maior que zero!")
                return False
        except ValueError:
            print(Fore.RED + "Por favor, digite um número válido!")
            return False

        # Verifica se o evento já existe
        try:
            with open("eventos.csv", "r") as arquivo:
                leitor = csv.reader(arquivo)
                next(leitor)  # Pula o cabeçalho
                for linha in leitor:
                    if linha[0].lower() == evento.lower():
                        print(Fore.RED + "Já existe um evento com este nome!")
                        return False
        except FileNotFoundError:
            pass

        with open("eventos.csv", "a", newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([evento, data, descricao, numero_maximo_participantes])
        print(Fore.GREEN + "Evento cadastrado com sucesso!")
        return True
        
    except Exception as e:
        print(Fore.RED + f"Erro ao cadastrar evento: {str(e)}")
        return False

def atualizar_evento():
    eventos = []
    evento = input(Fore.GREEN + "Digite o nome do evento que deseja atualizar: ")
    
    with open("eventos.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        eventos.append(next(leitor))
        evento_encontrado = False
        for linha in leitor:
            if linha[0] == evento:
                evento_encontrado = True
            eventos.append(linha)
    
    if not evento_encontrado:
        print(Fore.RED + "Evento não encontrado!")
        return False
        
    try:
        data = datetime.strptime(input(Fore.GREEN + "Digite a data do evento (dd/mm/aaaa): "), "%d/%m/%Y").date()
    except ValueError:
        print(Fore.RED + "Formato de data inválido! Use dd/mm/aaaa")
        return False
        
    descricao = input(Fore.GREEN + "Digite a nova descrição do evento: ")
    numero_maximo_participantes = int(input(Fore.GREEN + "Digite o novo numero maximo de participantes: "))
    
    for i in range(len(eventos)):
        if eventos[i][0] == evento:
            eventos[i] = [evento, data, descricao, numero_maximo_participantes]
            
    with open("eventos.csv", "w", newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(eventos)
        
    print(Fore.GREEN + "Evento atualizado com sucesso!")
    return True

def visualizar_inscricoes():
    try:
        with open("inscricoes.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)  # Pula o cabeçalho
            
            print(Fore.GREEN + "\nInscrições realizadas:")
            inscricoes_por_evento = {}
            
            for inscricao in leitor:
                evento = inscricao[1]
                if evento not in inscricoes_por_evento:
                    inscricoes_por_evento[evento] = []
                inscricoes_por_evento[evento].append(inscricao)
            
            for evento, inscricoes in inscricoes_por_evento.items():
                print(Fore.YELLOW + f"\nEvento: {evento}")
                print(Fore.WHITE + f"Total de inscritos: {len(inscricoes)}")
                print("Lista de participantes:")
                for inscricao in inscricoes:
                    print(f"- {inscricao[0]} (Data de inscrição: {inscricao[2]})")
                    
        return True
        
    except FileNotFoundError:
        print(Fore.RED + "Não há inscrições registradas!")
        return True
    except Exception as e:
        print(Fore.RED + f"Erro ao visualizar inscrições: {str(e)}")
        return False

def excluir_evento():
    try:
        evento_para_excluir = input(Fore.GREEN + "Digite o nome do evento que deseja excluir: ")
        
        # Verifica se o evento existe
        try:
            evento_existe = False
            with open("eventos.csv", "r") as arquivo:
                leitor = csv.reader(arquivo)
                next(leitor)  # Pula o cabeçalho
                for evento in leitor:
                    if evento[0].strip().lower() == evento_para_excluir.strip().lower():
                        evento_existe = True
                        evento_para_excluir = evento[0]  # Usa o nome exato do evento
                        break
                    
            if not evento_existe:
                print(Fore.RED + "Evento não encontrado!")
                return False
                
        except FileNotFoundError:
            print(Fore.RED + "Não há eventos cadastrados!")
            return False
        
        # Verifica se existem inscrições para o evento
        try:
            with open("inscricoes.csv", "r") as arquivo_inscricoes:
                leitor_inscricoes = csv.reader(arquivo_inscricoes)
                next(leitor_inscricoes)  # Pula o cabeçalho
                for inscricao in leitor_inscricoes:
                    if inscricao[1].strip().lower() == evento_para_excluir.strip().lower():
                        print(Fore.RED + "Não é possível excluir o evento pois existem inscrições vinculadas a ele!")
                        return False
        except FileNotFoundError:
            pass
            
        # Se chegou aqui, pode excluir o evento
        eventos = []
        with open("eventos.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            eventos.append(next(leitor))  # Mantém o cabeçalho
            
            for evento in leitor:
                if evento[0] != evento_para_excluir:
                    eventos.append(evento)
                    
        with open("eventos.csv", "w", newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(eventos)
            
        print(Fore.GREEN + "Evento excluído com sucesso!")
        return True
        
    except Exception as e:
        print(Fore.RED + f"Erro ao excluir evento: {str(e)}")
        return False

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
                print(f"Vagas totais: {evento[3]}")
                print(f"Vagas restantes: {vagas_restantes}")
                
        return True
        
    except FileNotFoundError:
        print(Fore.RED + "Não há eventos cadastrados!")
        return True
    except Exception as e:
        print(Fore.RED + f"Erro ao listar eventos: {str(e)}")
        return False
