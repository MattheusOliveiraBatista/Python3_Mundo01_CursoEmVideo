'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)


PrimeiroValor = int(input('Digite o Primeiro Valor: '))
SegundoValor = int(input('Digite o Segundo Valor: '))
TerceiroValor = int(input('Digite o Terceiro Valor: '))

if PrimeiroValor < SegundoValor + TerceiroValor and SegundoValor < PrimeiroValor + TerceiroValor and TerceiroValor < SegundoValor + PrimeiroValor:
    print('Os segmentos acima PODEM FORMAR um triângulo!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')