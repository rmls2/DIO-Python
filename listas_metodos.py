lista_numerica = [2, 3, 2, 10, 15, 27, 32, 64, 142, 76 ]
lista_strings = ['a', 'c', 'da', 'la', 'casa']

#len (): é uma função built-in que conta o numero de elementos de um iterável: lista, tuplas, set 

print('esse é o tamanho da lista numérica:',len(lista_numerica))
# append: add um elemento a uma lista 

lista_strings.append('b')

#copy : vai copiar a lista

numerica_copiada = lista_numerica.copy()
print(numerica_copiada)

# clear (): vai limpar toda a lista 

numerica_copiada.clear()

print('essa é a lista copiada: ', numerica_copiada)

# count (<elemento>): vai contar um determinado os elemento da lista 

print(lista_numerica.count(2))

# extend(<listaext>): vai agregar <listaext> a outra lista 

lista_numerica.extend([2,3,5,7])

print(lista_numerica)

# index(<elemento>): retorna o primeiro indicie de um elemento de uma lista

print(lista_numerica.index(15))

# pop(): remove o último elementto da lista (a lista é implementada como uma pilha em python), mas tbm é possível passar um
# indice de um elemento específico dentro de pop. Essa função não só remove como ela tbm retorna o valor removido 

valor_removido = lista_numerica.pop(6)

print(valor_removido)

# remove(<elemento>): remove um elemento específico, mas não retorna nada 

x = lista_numerica.remove(15)
print(x) ## isso aqui printa None, ja que remove não retorna nada 

print(lista_numerica)

# reverse(): é um metodo que vai espelhar os elementos da lista, ou seja vai colocar o que ta no fim no começo e o que ta no começo no fim 

""" print(lista_numerica)
lista_numerica.reverse()
print(lista_numerica) """

# sort(): ordena uma lista, não retorna nada, mas ordena a lista toda.  
print(lista_numerica)
lista_numerica.sort()
print(lista_numerica)

print(lista_strings)
lista_strings.sort()
print(lista_strings)

## passando parâmetros para o sort 
print('\nsort com parâmetros: \n')

print(lista_strings)
lista_strings.sort(reverse=True) #ordena em ordem contrária (lexical)
print(lista_strings)
print('')
print(lista_strings)
lista_strings.sort(key= lambda x: len(x)) ##ordena pelo tamanho dos elementos do menor pro maior a partir dos primeiros menores
print(lista_strings)

#sort usando os dois parametros key e reverse: nesse caso o parâmetro de tamanho vai se sobre sair em relação ao lexical


lista = ['python','comida','domidas', 'ab','ac', 'a', 'jaca'] #a, ab, ac, jaca, python, comida >> ['domidas', 'python', 'comida', 'jaca', 'ab', 'ac', 'a']
print(lista)
lista.sort(key= lambda x: len(x), reverse=True)
print(lista)


# sorted(): é uma função built-in que serve para ordenar iteráveis, funciona igual ao método sort()