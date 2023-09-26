# .clear() : vai limpar o dicionario, eliminar todos os itens


contatos = {
    'miller182@': {'nome': 'Robert', 'idade': 26},
    'karol@': {'nome': 'Karolyne', 'idade': 26},
    'gabghv@': {'nome': 'Gabriel', 'idade': 22},
    'bruno@': {'nome': 'Bruno', 'idade': 23} 
}

# contatos.clear()
# print(contatos)

# .copy(): vai fazer uma copia 
copia = contatos.copy()

copia['miller182@'] = {'nome': 'Miller'}

# print(copia)
# print(contatos)

# Método de definir chaves para um dicionario sem passar um valor logo de cara ou passando um valor padrão 
dic = dict.fromkeys(["cpf", "telefone"])
dic2 = dict.fromkeys(["cpf", "telefone"],'vazio') #passando um valor padrao 

# print(dic2)

# .get(): se o metodo não encontrar a chave ele irá retornar None


# print(copia['telefone']) #keyerror, pois a chave telefone não exite 

# print(copia.get('telefone')) #retorna None porque essa chave não existe 
# print(copia.get('telefone', 'valor default')) #é possível tbm ele retornar um valor default

## .keys(): retorna um iterável cujo elementos são as chaves dos dicionários 

# print(contatos.keys())

## .items(): retorna uma um iteravel cujos elementos são tupla de chave e valor 

# print(contatos.items())

## values(): retornta um iterável com os valores 
# print('valores: ', contatos.values())

## .pop(<item>): remove e retornar o valor removido, caso não encontre a chave é possível passar um valor default que ele irá retornar 
## caso o valor procurado para remoção não seja encontrado é possível passar um valor defaultp pra ele retornar e assim evitar o keyerror

print(contatos.pop('gabghv@'))
print(contatos.pop('gabghv@', 'chave não encontrada')) #passando valor default

## .popitem(): remove os itens do dicionário seguindo uma sequencia de trás para frente e retorna-o

# print(contatos)
# print(contatos.popitem())
# print(contatos.popitem())
# print(contatos.popitem())

## .setdefault(<chave>, <valor>): add uma chave valor, se a chave passada não existir. Caso o valor ja exista, ele não vai alterar nada

dic.setdefault('idade', None) #como não existia a chave 'idade', ele add no dicionario 
print(dic)

dic.setdefault('idade', '22')  #como idade é uma chave que existe ele não faz nada. 
print(dic)

## update({<chave1>: <valor1>, ...}): vai atualizar o dicionário com as chaves e valores definidos dentro de update()

dic.update({'cpf': 12}) #como só foi passado um valor, ele só irá atualizar um único valor.
print(dic)


## Verificando a existencia de chaves dentro de um dicionario. 

print(contatos)


if 'miller182@' in contatos: 
    print('a chave existe dentro desse dicionario')

if 'nome' in contatos['miller182@']: 
    print('a chave existe dentro desse dicionario')



## del: apaga todo o objeto: se colocar <dicionario>[<chave>] ele apaga todo esse objeto: chave e valor
## se colocar só del <dicionario> ele vai apagar o dicionario inteiro 

teste_dic = {'a': 10, 'b': 30, 'c': 40, 'd': 50}

print(teste_dic)

del teste_dic['b']

print(teste_dic['a'])