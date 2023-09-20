"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere) (><^)(quantidade)
> - Esquerda
< - Direita
^- Centro
Sinal - + ou -
Ex. 0>-100, .1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.48765461231546:.1f}')
print(f'O hexadecimal de 1500 é {1500:04X}')


