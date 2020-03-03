#!/usr/bin/python3

## Functions

# Define a funcao
def sum(x=3, y=5):
	print("x: " + str(x))
	print("y: " + str(y))
	return x + y

# Chamada simples de funcao
x = 1
y = 2
z = sum(x, y)
print(z)

# Chamada de funcao com parametro sem ordem
z = sum(y=10, x=13)
print(z)

# Utiliza valor padrao dos parametros
z = sum()
print(z)

# Atribuicao para mais de uma variável
a, b = x, y
print('a: {}; b:{}'.format(a, b))

list = [1, 2, 3]
a, b, c = list
print('a: {}; b:{}; c:{}'.format(a, b, c))

# troca de valores
a, b = b, a
print('a: {}; b:{}'.format(a, b))

## Conditionals

temperature = 4
if temperature <= 0:
	print('Solido')
elif temperature > 0 and temperature < 100:
	print('Liquido')
else:
	print('Gasoso')

# Notacao matematica
if 0 < temperature < 100:
	print('Liquido')

###
# Exercicios
###

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.

def verificaListaIguais(lista1, lista2):

	if lista1 == lista2:
		return True
	else:
		return False

lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
print(verificaListaIguais(lista1, lista2))


# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.

def verificaPalindrome(string1, string2):
	string1 = string1.replace(" ", "").lower()
	string2 = string2.replace(" ", "").lower()
	string1Invertida = string1[::-1]
	string2Invertida = string2[::-1]

	if string1 == string1Invertida and string2 == string2Invertida and string1 == string2Invertida:
		return True
	else:
		return False

string1 = 'luzazul'
string2 = 'luz Azul'

print(verificaPalindrome(string1, string2))

# OBS.: Utilize apenas o que foi estudado ate agora
