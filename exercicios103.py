## STRINGS
## https://docs.python.org/3/tutorial/introduction.html#strings

msg = 'Minimal Techno Tripping'
size = len(msg)
print('Tamanho de msg:')
print(size)

## Converter para string
s = str(42)
print(s)

s = 'I like you'
print(s)

## Examine as strings colocando prints
s2 = s[0]  # retorna 'I'

s2 = len(s)  # retorna 10

# Como jah fizemos com as listas
s2 = s[0:7]  # retorna 'I like '

s2 = s[6:]  # retorna 'you'

s2 = s[-1]  # retorna 'u'


## concatenar strings
s3 = 'The meaning of life is'
s4 = '42'
s5 = s3 + ' ' + s4       # retorna 'The meaning of life is 42'
s5 = s3 + ' ' + str(42)  # same thing

# split a string into a list of substrings separated by a delimiter

s = 'Anything you want it to be'
s.split(' ')        # retorna ['Anything', 'you', 'want', 'it', 'to', 'be']
s.split()           # idem


## Entrada via teclado (caracter de escape -> '\')
# print('What\'s your name?')
# nome = input()
# sobrenome = 'Abreu'
# print('Hi, ' + nome)
# print('Hi,', nome)
#
## Formatacao com o metodo format
# msg = 'Hi, {1} {0}!'.format(nome, sobrenome)
# print(msg)


## Inverter a string
string = 'Hello, my friend!'
print(string)
string2 = string[::-1]
print(string2)

## Substituir
cheese_str = 'I like cheese'
print(cheese_str)
new_cheese_str = cheese_str.replace('like', 'love')
print(new_cheese_str)

###
# Exercicios
###

book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

# 1) Extraia o titulo do livro da string
titulo = book1.split(' by ')
print(titulo[0])

# 2) Salve o titulo de cada livro em uma variável
titulo = book1.split(' by ')
tituloBook1 = titulo[0]

titulo = book2.split(' by ')
tituloBook2 = titulo[0]

titulo = book3.split(' by ')
tituloBook3 = titulo[0]

# 3) Quantos caracteres cada título tem?
print(tituloBook1.__len__())
print(tituloBook2.__len__())
print(tituloBook3.__len__())

# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}
ano = book1.split(', ')
anoBook1 = ano[1]
titulo = book1.split(' by ')
tituloBook1 = titulo[0]
autor = book1.split(' by ')
autorAuxiliar = autor[1].split(', ')
autorBook1 = autorAuxiliar[0]

informacoes = '{0} - {1} - {2}'.format(tituloBook1, autorBook1, anoBook1)
print(informacoes)

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'.lower()
palindrome_three = 'luz azul'.strip(" ")
palindrome_four = 'caneta azul'.strip(" ")

palindrome1 = palindrome_one[::-1]
palindrome2 = palindrome_two[::-1]
palindrome3 = palindrome_three[::-1]
palindrome4 = palindrome_four[::-1]

if palindrome1 == palindrome_one:
	print(palindrome1 + ' é igual a ' + palindrome_one)
if palindrome2 == palindrome_two:
	print(palindrome2 + ' é igual a ' + palindrome_two)
if palindrome3 == palindrome_three:
	print(palindrome3 + ' é igual a ' + palindrome_three)
if palindrome4 == palindrome_four:
	print(palindrome4 + ' é igual a ' + palindrome_four)
