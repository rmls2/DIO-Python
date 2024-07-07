## tuplas: é uma estrutura de dados em python que são imutáveis 

# formas de criar uma tupla 

frutas = ('laranja', 'manga', 'uva', 'maçã', 'uva', 'laranja', 'uva') # usar uma virgula no final de uma tupla é uma boa prática
tupla1 = tuple('Python') #transforma os caracteres em um elemento da tupla
tupla2 = ('Brasil',) # assim é uma tupla 
nao_e_uma_tupla = ('Brasil') # sem a virgula no final o python trataria isso como uma string
# print(type(tupla2)) 

# o acesso a uma tupla é igual ao acesso de um elemento de uma lista

frutas[0] # retorna o primeiro elemento 
frutas[-1] #retorna o último elemento

# tuplas aninhadas 
## tuplas podem armazenar todo tipo de objeto, inclusive outras tuplas 


tuplas_aninhada1 = ('cor', 'mato', ['george', 'paul', 'ringo', 'john'], ('guitarra', 'bateria', ('cordas','capotraste')))

# print(tuplas_aninhada1[3][2][0])

## fatiamento de tuplas 

print(frutas[0:2])
print(frutas[2:4])

## tuplas também podem usar outros métodos de lista como len, enumerate, count etc. E os outros métodos imutáveis de lista 

for i,j in enumerate(frutas):
    print(f'{i}: {j}')


print(frutas.count('uva'))