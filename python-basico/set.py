## conjuntos: coleção de objetos que só possuem elementos únicos

conjunto1 = set([1,2,3,4,3,2,4,4]) #construindo um conjunto com a função built-in set

conjunto2 = set('casamento') #cria um set, mas não vai colocar cada caractere na mesma ordem que ta a string

conjunto3 = set((1,20,31,45,52)) 


# obs: o conjunto não preseerva a ordem dos elementos

# print(conjunto3)

## Acessando elementos de um conjunto em python

# conjuntos não possuem indexação, assim para acessar os valores de um conjunto é preciso transformá-lo primeiro
# para uma lista 

lista_de_conjunto = list(conjunto1)
# print(lista_de_conjunto[0])

## iterar sobre conjuntos 

# for i in conjunto1:
#     print(i)

## apesar de não ser possível indexar listas, é possível usar o método enumerate() para percorrer uma lista e enumerar 
# seus elementos 

for i, j in enumerate(conjunto1):
    print(f'esse é o "indice"{i}, esse é o elemento {j}')












