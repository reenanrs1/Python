#arquivos
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    conteudo = arquivo.read()
    arquivo.close()
    print(f"Lendo o arquivo {nome_arquivo}:")
    print(conteudo)
    
def escrever_arquivo(nome_arquivo, conteudo):
    arquivo = open(nome_arquivo, "w")
    arquivo.write(conteudo)
    arquivo.close()
    print(f"Arquivo {nome_arquivo} criado com sucesso!")

def adicionar_conteudo(nome_arquivo, conteudo):
    arquivo = open(nome_arquivo, "a")
    arquivo.write(conteudo)
    arquivo.close()
    print(f"Conteúdo adicionado ao arquivo {nome_arquivo} com sucesso!")

def ler_linha_arquivo(nome_arquivo):
    print(f"Lendo o arquivo {nome_arquivo}:")
    for linha in open(nome_arquivo, "r"):
        print(linha.strip()) #strip remove os espaços em branco

ler_arquivo("Modulo4/Aula2/cidades.txt")
escrever_arquivo("Modulo4/Aula2/cidades.txt", "Campinas\n")
ler_arquivo("Modulo4/Aula2/cidades.txt")
adicionar_conteudo("Modulo4/Aula2/cidades.txt", "São Paulo\n")
ler_arquivo("Modulo4/Aula2/cidades.txt")
ler_linha_arquivo("Modulo4/Aula2/cidades.txt")


# O que é manipulação de arquivos?
#A manipulação de arquivos em programação refere-se à capacidade de abrir, ler, escrever, atualizar e fechar arquivos em um sistema. 
# Trabalhar com arquivos é fundamental em aplicações de software que envolvem o armazenamento e recuperação de dados.

# Tipos de arquivos
# Texto: Arquivos que contêm dados de texto, como documentos, relatórios e mensagens.
# Binário: Arquivos que contêm dados não-textuais, como imagens, áudios e vídeos.
# CSV: Arquivos que contêm dados separados por vírgulas, como tabelas de banco de dados.
# JSON: Arquivos que contêm dados em formato de objeto JavaScript, como configurações e dados estruturados.
# XML: Arquivos que contêm dados em formato de tags, como configurações e dados estruturados.

# Modos de abertura de arquivos
# "r": Abre o arquivo para leitura.
# "w": Abre o arquivo para escrita. Se o arquivo não existir, ele será criado.
# "a": Abre o arquivo para escrita. Se o arquivo não existir, ele será criado.
# "x": Abre o arquivo para escrita. Se o arquivo já existir, ocorre um erro.
# "b": Abre o arquivo em modo binário.
# "t": Abre o arquivo em modo texto.

#usando read()
#arquivo = open("Modulo4/Aula2/cidades.txt", "r")
#conteudo = arquivo.read()
#print(conteudo)
#arquivo.close()

#Usando readline()
#arquivo = open("Modulo4/Aula2/cidades.txt", "r")
#linha = arquivo.readline()
#print(linha)
#arquivo.close()

#usando readlines()
#arquivo = open("Modulo4/Aula2/cidades.txt", "r")
#linhas = arquivo.readlines()
#print(linhas)
#arquivo.close()

#escrevendo em um arquivo
#usando write()
#arquivo = open("Modulo4/Aula2/cidades.txt", "w")
#arquivo.write("São Paulo\n")
#arquivo.close()

#usando writelines()
#arquivo = open("Modulo4/Aula2/cidades.txt", "w")
#arquivo.writelines(["São Paulo\n", "Campinas\n", "Jandira\n", "Itapevi\n", "Mogi Mirim\n"])
#arquivo.close()

#usando append()
#arquivo = open("Modulo4/Aula2/cidades.txt", "a")
#arquivo.write("São Paulo\n")
#arquivo.close()
    



