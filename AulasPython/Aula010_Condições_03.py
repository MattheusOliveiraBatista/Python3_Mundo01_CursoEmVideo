'''
Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.
'''
n1 = int( input('Digite a primeira nota: '))
n2 = int( input('Digite a segunda nota: '))

m = (n1 + n2)/2

print('A sua média foi {:.1f}'.format(m))

if m >= 6.0:
    print('Sua média foi boa! Parabéns!!')
else:
    print('Sua média foi ruim! Estude Mais!! :(')