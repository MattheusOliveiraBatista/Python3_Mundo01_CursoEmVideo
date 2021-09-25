'''
Nessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), 
transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().
'''

frase = 'Curso em Video Python'
#Começa no índice 9 e vai até o 20, saltando de 2 em 2
print(frase[9:21:2]) 

#Começa no índice 3 e vai até o final, saltando de 3 em 3
print(frase[9::3])

#Fatiamento de String
trecho_01 = frase[0:5]
trecho_02 = frase[6:8]
trecho_03 = frase[9:14]
trecho_04 = frase[15:]


print(trecho_01)
print(trecho_02)
print(trecho_03)
print(trecho_04)

#Tamanho ou comprimento
print(len(frase))

#Contar quantas vezes tem o "o"
#ou frase.count('o', 0, 13)
print(frase.count('o'))

#Encontrar - find
#retorno -1, significa que não tem a string na frase
print(frase.find('deo'))

#Procurando curso dentro da string frase
print('curso' in frase)

#substituindo palavras na string- não substitui 
print(frase.replace('Python','Android'))
print(frase)

#Letras maiúsculas
print(frase.upper())

#Letras minúsculas
print(frase.lower())

#Apenas a primeira letra maiúscula
print(frase.capitalize())

#A próxima letra após o espaçamento será maiúscula
print(frase.title())


#Remove os espaços finais e iniciais desnecessários
frase_02 = 'Aprendo Python'
print(frase_02.strip())
#rstrip - remove apenas os espaços da direita
#lstrip - remove apenas os espaços da esquerda

#Quebra de várias strings - caractere de quebra é o espaçamento
dividido = frase.split()
print(dividido[2][2])

#Juntando a string novamente
print(' '.join(frase))