def ler_cidades():
    cidades = []
    for linha in open("Modulo4/Projeto/cidades.csv", "r"):
        cidades.append(linha.strip().lower())
    return cidades
