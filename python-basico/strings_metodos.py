# '<criterio>'.join(<objeto-iterável>): vai unir todos os itens da lista/iterável  de acordo com o criterio 
lista = ['python','comida','domidas', 'ab','ac', 'a', 'jaca']
uniao = '--'.join(lista)
print(uniao)
print(type(uniao))

dico = {'a':1, 'b': 2}
uniao2 = '--'.join(dico.keys())
print(uniao2)
print(type(uniao2))

# .split('<condiçao>'): vai dividir uma string em várias strings de acordo com uma condição:

stringtest='cabeca-de-gelo'

resultado1, resultado2, resultado3 = stringtest.split('-')  #se passássemos só uma variável, teriamos uma lista com três items ['cabeca','de','gelo']

print(resultado1)
print(type(resultado1))
print(resultado2)
print(type(resultado2))
print(resultado3)
print(type(resultado3))