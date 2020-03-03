
'''
	DESAFIO!!!
	1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!
	2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999. Depois crie um loop para percorrer a lista ateh encontrar o primeiro multiplo de 5.
	OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

# Desafio 1
lista = list(range(0,2000, 2))

# print(lista)
print(lista.__len__())

# Desafio 2
lista2 = list(range(1, 9999))

for i in lista2:
	if(i%5 == 0):
		print(i, 'é múltiplo de 5.')
