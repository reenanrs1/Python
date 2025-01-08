nota = float(input('Digite a sua nota: '))
frequencia = float(input('Digite a sua frequência: '))

if nota >= 5 and frequencia >= 75:
    situacao ='Aprovado'
elif nota < 5 and frequencia >= 75:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'

print(f'Você está: {situacao} !')