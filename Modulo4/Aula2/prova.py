def quadrado(x):
    return x * x

resultado = quadrado(quadrado(2))
print(resultado)

def calc(a,b=2):
    return a ** b

resultado = calc(5,3)
print(resultado)

def saudacao(nome):
    return f"Olá, {nome}!"
print(saudacao("Carlos"))


with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!")
arquivo.read()
