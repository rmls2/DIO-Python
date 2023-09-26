## dicionario: conjunto não-ordenado de pares de chaves e valores.

#formas de declarar um dicionario

pessoa = {"nome": "Robert", "idade": 26}
pessoa = dict(nome = "Robert", idade = 26)

dicio = {'a': 10, 'b': 30, 'c': 40, 'd': 50}

## os dados são acessados por meio das chaves

print(pessoa["nome"])

##e são modifcados mudando o seu valor atribuido a chave
pessoa["nome"]= "Miller"

print(pessoa["nome"])

## Dicionarios podem armazenar qualquer tipo de objetos em python como valor desde que a chave para esse objeto seja algo imutável (como numeros ou strings ) 
## com isso é possível aninhar dicionarios 

dic_aninhado = {"nome": "Robert", "carcterísticas": {"peso": 104, "tipo físico": 'Gordo'}}

x = dic_aninhado["carcterísticas"]["tipo físico"]

print(x)

# iterando sobre dicionarios 

# só pela chave
for chave in dicio:
    print(f'{chave}: {dicio[chave]}')

# usando items(): que retorna a chave o valor para cada iteração
for chave, valor in dicio.items():
    print(f'{chave}: {valor}')

x = dicio.items()
print(type(x))