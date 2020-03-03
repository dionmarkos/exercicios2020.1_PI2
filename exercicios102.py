weekdays = ['mon','tues','wed','thurs','fri']

# print(weekdays)
# print(type(weekdays))

days = weekdays[0]         # elemento 0
days = weekdays[0:3]       # elementos 0, 1, 2
days = weekdays[:3]        # elementos 0, 1, 2
days = weekdays[-1]        # ultimo elemento

test = weekdays[3:]        # elementos 3, 4

weekdays

days = weekdays[-2]        # ultimo elemento (elemento 4
days = weekdays[::]        # all elementos
days = weekdays[::2]       # cada segundo elemento (0, 2, 4)
days = weekdays[::-1]      # reverso (4, 3, 2, 1, 0)

all_days = weekdays + ['sat','sun']     # concatenar

# print(all_days)

# Usando append
days_list = ['mon','tues','wed','thurs','fri']
days_list.append('sat')
days_list.append('sun')

# print(days_list)
# print(days_list == all_days)

list = ['a', 1, 3.14159265359]
# print(list)
# print(type(list))
# list.reverse()
# print(list)

#########
# Exercícios - Listas
# Faça sem usar loops
#########

print('\nComo selecionar "wed" pelo indice?')
print( weekdays[2] )

print('\nComo verificar o tipo de "mon"?')
print( type(weekdays[0]) )

print('\nComo separar "wed" até "fri"?')
print( weekdays[2:5] )

print('\nQuais as maneiras de selecionar "fri" por indice?')
print( weekdays[4] )
print( weekdays[-1] )
print( weekdays.__getitem__(weekdays.index('fri')) )

print('\nQual eh o tamanho dos dias e days_list?')
print( days.__len__() )
print( days_list.__len__() )

print('\nComo inverter a ordem dos dias?')
days.reverse()
print( days )

print('\nComo inserir a palavra "zero" entre "a" e 1 de list?')
list.insert(1, 'zero')
print(list)

print('\nComo atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?')
print(list)
ultimo_elemento = list[-1]
list.remove(list[-1])
print(list)
print(ultimo_elemento)

print('\nComo limpar list?')
list = []
print(list)

print('\nComo deletar list?')
del list
