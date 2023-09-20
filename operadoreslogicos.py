#Operadores Lógicos
#and (e) or (ou) not (não)
#and - todas as condições precisam ser verdadeiras
#se qualquer valor for considerado falso, a exporesão inteira será avaliada naquele valor
#são considerados falsy  0 0.0 '' False
# também existe o tipo de None que é 
#usando para representar um não valor
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input ('Senha: ')

senha_permitida = '123456'
#if True:
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


senha = input('Senha: ') or 'Sem senha'
print(senha)