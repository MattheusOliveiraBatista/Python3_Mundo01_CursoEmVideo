'''
Nessa aula, vamos aprender como funcionam os tipos primitivos no Python e as peculiaridades do int() float() bool() e str(). 
Além disso, veremos como fazer as primeiras operações com a função print() do Python.
'''



#Tipos primitivos

#int - 7 -4 0 9875
# flaot 4.5 0.076 -15.223 7.0
#bool True False
#str 'Olá' '7.5' ''

int 
float
bool 
str


#Tipos diferentes de print
s = 10

print('A soma vale',s)
print( 'A soma vale {}'.format(s))

#Tipo Primitivo- type

#Int
n1 = int(input('Digite o numero:'))
print('{} é do tipo{}'.format(n1, type(n1)))

#Float
n1 = 3.14
print('{} é do tipo {}'.format(n1, type(n1)))

#Bool 
n1 = True
print('{} é do tipo {}'.format(n1, type(n1)))

#String
n1 = 'Olá Mundo!'
print('{} é do tipo {}'.format(n1 ,type(n1)))
