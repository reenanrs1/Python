#Lendo arquvos csv
#import csv
#with open("Modulo4/Aula2/cidades.csv", "r") as arquivo:
#    leitor = csv.reader(arquivo)
#    for linha in leitor:
#        print(linha)

#escrevendo em um arquivo csv
import csv
with open("Modulo4/Aula2/cidades.csv", "w") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["cidade", "estado"])
    escritor.writerow(["São Paulo", "SP"])
    escritor.writerow(["Campinas", "SP"])

#Lidando com exceções
try:
    arquivo = open("Modulo4/Aula2/cidades1.csv", "r")
    print(arquivo.read())
except FileNotFoundError:
    print("Arquivo não encontrado")

#fechando arquivos
arquivo.close()

#usando with
with open("Modulo4/Aula2/cidades.csv", "r") as arquivo:
    print(arquivo.read())

#leitura linha a linha
#with open("Modulo4/Aula2/cidades.csv", "r") as arquivo:
#    for linha in arquivo:
#        print(linha)

#leitura em blocos
#with open("Modulo4/Aula2/cidades.csv", "r") as arquivo:
#    while True:
#        bloco = arquivo.read(100)
#        if not bloco:
#            break
#        print(bloco)

