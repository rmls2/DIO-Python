# formas de esrever listas
lista_sem_list = []
lista_com_list = list(range(10))
print(lista_com_list)

# fatiamentos 

lista_metade1 = lista_com_list[:5]
lista_metade2 = lista_com_list[5:]
metade2_reversa  = lista_metade2[::-1]

# é possível passar um argumento step ao final do fatiamento 

lista_com_list[0:5:2]  ##vai de 0 até 5 pulando de 2 em 2 [inicio: parada: step ]

print(lista_com_list[0:8:2])


print('essa é a primeira metade: ', lista_metade1)
print('essa é a segunda metade: ', metade2_reversa)

# listas aninhadas: é uma lista de listas e podem ser usadas para representar tabelas ou matrizes

listas_de_listas = [[1,2,3], [4,5,6], [7,8,9]]

print(listas_de_listas[1][-1]) ##vai retornar 6 

#percorrendo listas com indices usando a função enumerate que tbm tem um indice e é uma classe especifica de python


carros = ['celta', 'uno', 'strada', 'palio']

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

## compressão de listas (liste comprehension)
# é útil quando se precisa gerar uma nova lista a partir de uma existente ou quando se pretende alterar os valores da lista
# original e criar uma nova lista 


lista_numerica = [2, 75,18, 26, 38, 42, 10]
lista_pares = []
lista_qualquer = []

""" for i in lista_numerica:
    if i%2==0:
        lista_pares.append(i)

print(lista_pares) """

# usando list comprhension pro código acima 

""" lista_pares = [i for i in lista_numerica if i%2 ==0]
print(lista_pares) """

""" for i in lista_numerica:
    lista_qualquer.append(i-1)
print(lista_qualquer) """

# usando list comprehension 

lista_qualquer = [(i-1) for i in lista_numerica]
print(lista_qualquer)