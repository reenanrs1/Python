# Operadores in e not in
# string são iteráveis - negocio que pode navegar item por item
# 0 1 2 3 4 5
# O t á v i o
#-6-5-4-3-2-1

#nome  = 'Otávio'
#print (nome[2])
#print (nome[-4])
#print('á' in nome) # True verifica se a letra á está entre
#print('z'in nome) # False
#print(10 * '-')
#print ('vio' not in nome)
#print(10 * '-')


nome = input('Digite seu nome:')
encontrar = input ('Digite o que deeja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
