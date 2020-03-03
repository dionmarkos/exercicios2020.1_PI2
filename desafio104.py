
'''
	DESAFIO!!!
	1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.
	2) Agora faca sem utilizar uma terceira variavel temporaria.
	OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''
# Com variável auxiliar

a = 1
b = 2

aux = a
a = b
b = aux

print(a)
print(b)

# Sem variável auxiliar

x = 1
y = 2

x, y = y, x

print(x)
print(y)
