'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 
'''
import math

angulo = float(input('Digite o ângulo que deseja calcular: '))

AnguloSeno = math.sin(math.radians(angulo))
AnguloCosseno = math.cos(math.radians(angulo))
anguloTangente = math.tan(math.radians(angulo))

print(20*'*', '\n')
print('O ângulo de {} tem o Seno de {:.2f}'.format(angulo, AnguloSeno))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(angulo, AnguloCosseno))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(angulo, anguloTangente))
print('\n')
print(20*'*')
