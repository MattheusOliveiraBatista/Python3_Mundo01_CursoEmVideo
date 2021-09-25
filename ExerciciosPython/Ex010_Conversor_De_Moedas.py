'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 
'''

dinheiro = float (input('\nDigite seu saldo em R$: '))

dolares = dinheiro/3.27

print('Seu saldo em R$ {:.2f} são {:.2f} dólares'.format(dinheiro,dolares))