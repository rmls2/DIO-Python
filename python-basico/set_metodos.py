# Métodos da classe set 

## .union(): une dois conjuntos 

conj1 = {1,2,3,5}
conj2 = {1,2,4,6}

uniao = conj1.union(conj2)

# print(uniao)

## .intersection()

intersec = conj1.intersection(conj2)

# print(intersec)

## .difference(): vai fazer a diferença dos conjuntos
## diferença A - B = tudo que ta em A e não ta em B

print(conj1.difference(conj2))

## .symmetric_difference(): retira o que está na interseção dos dois conjuntos e retorna o complemento da interseção. 

print(conj1.symmetric_difference(conj2))

##  .issubset(): retorna true se um conjunto_a é um subconjunto de um conjunto_b
## issuperset(): retorna true se um conjunto_a contem um conjunto_b
## isdisjoint(): retornta true se os dois conjuntos avaliados são disjuntos 
conj_a = {1,2,3,4}
conj_b = {1,2,3,4,5,6,7,8}

print(conj_b.issubset(conj_a))
print(conj_b.issuperset(conj_a))
print(conj_b.isdisjoint(conj_a))

## .add(<elemento>): add um elemento a um conjunto

conj_c = {2,3}

conj_c.add(6)

print(conj_c)

## .clear(): vai limpar o conjunto e retorna ele vazio. 

# conj_c.clear()
# print(conj_c)

## .copy(): vai retornar uma cópia de um conjunto usado ao aplicar o método

conj_d = conj_c.copy()
print(conj_d)

## .discard(<elemento>): retira o elemento do conjunto, mas não retorna nada. Se o elemento descartado não estiver no conjunto a função não dá erro

print(conj_b)
conj_b.discard(8)
print(conj_b)

## .pop(): retira o elemento do conjunto e retorna o elemento retirado. Diferente da lista, começa a retirar do começo.

conj_b.add(8)

conj_b.pop()

print(conj_b)

## .remove(<elemento>): remove o elemento tipo o descard, mas se o elemento passado não existir ele dará erro. retorna None

print(conj_b.remove(5))
print('conjunto_b com o elemento "5" removido: ', conj_b)

## .len(): retorna o tamanho do conjunto

print('o tamanho do conjunto_b é: ', len(conj_b))

## in: também é usado pra saber se um elemento está no conjunto 

print(5 not in conj_b)

