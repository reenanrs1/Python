#Manipulando dicionários
#Um dicionário é uma estrutura de dados que armazena pares de chave-valor. Cada chave é única e
# mapeia diretamente para um valor. Dicionários são amplamente utilizados quando precisamos buscar, 
# adicionar ou modificar dados rapidamente com base em uma chave.

cliente = {
    'nome': 'João', 
    'idade': 25, 
    'email': 'joao@gmail.com'
    }
print(cliente['nome'])

#Modificando um valor
cliente['nome'] = 'Pedro'
print(cliente)

#deletando uma chave
del cliente['email']
print(cliente)

if 'idade' in cliente:
    print(f'O cliente tem {cliente["idade"]} anos')
else:
    print('Idade não existe')

print("Lista de chaves")
for key in cliente.values():
    print(f'{key}')

print("Lista de Valores")
for key, value in cliente.items():
    print(f'{key}: {value}')

###############################################################

print(cliente.get('nome'))
######################################
#Trabalhando com api

#import json
#dados_json = '{"nome": "João", "idade": 25, "email": "joao@gmail.com"}'
#dados = json.loads(dados_json)
#print(dados)

