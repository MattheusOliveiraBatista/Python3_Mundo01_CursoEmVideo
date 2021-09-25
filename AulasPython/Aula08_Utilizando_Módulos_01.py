''''
Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. 
Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas
utilizando
'''

import math

#Importando apenas a função de raiz quadrada e floor
#from math import sqrt, floor

num = int(input('Digite um número: '))

raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num,raiz))

#Arredondando para cima
print('\nArredondando para cima - ceil \nA raiz quadrada de {} é igual a {}'.format(num,math.ceil((raiz))))

#Arredondando para baixo
print('\nArredondando para baixo - floor \nA raiz quadrada de {} é igual a {}'.format(num,math.floor((raiz))))
