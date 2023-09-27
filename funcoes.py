## funções são blocos de códigos em python que nos permite reutilizar o código que está dentro desse bloco sempre que necessário.
## as funções podem ter ou não parâmetros e retornar ou não valores. Quando programamos fazendo uso de funções se diz que programamos de maneira
## estruturada isso é um paradigma de programação 


def exibir_mensagem1():
    print('seja bem-vindo(a)!')

def exibir_mensagem2(nome):
    print(f'seja bem-vindo(a), {nome}!')

def exibir_mensagem3(nome='arnaldo'):   #isso aqui é chamado de argumento nomeado
    print(f'seja bem-vindo(a), {nome}!')

# exibir_mensagem1()
# exibir_mensagem2('cadu')
# exibir_mensagem3('tamanduá')


if exibir_mensagem1 == None:
    print('exibir_mensagem retorna vazio!')

## para retornar algum valor em função usamos a palavra reservada return. se uma função não tem um retorno explícito, ela retorna none.
# if exibir_mensagem1 == None:
#    print('exibir_mensagem retorna vazio!')

## em python não precisamos especificar o tipo de retorno que uma função pode ter e nem que tipo de parâmetro iremos usar 

def soma(a,b):
    return a+b

# print(soma([2,2],[3,3]))
# print(soma((2,2),(3,3)))
# print(soma(2,3))

## se uma função retorna mais de um valor ela retorna uma tupla, ja que uma tupla é uma estrutura imutável  

## Parâmetros: podem ser posicionais ou nomeados 

# argumento nomeado: perimite colocar um valor padrão para um parâmetro, como também permite trocar a ordem dos parâmetros 

def definir_carro(nome, marca, ano, placa):
    print('as características do carro são: nome: {} | marca: {} | ano: {}| placa: {}'.format(nome, marca, ano, placa))

# sem o uso do argumento nomeado a ordem dos parâmetros precisa se manter, para que cada argumento esta no lugar certo.
definir_carro('Palio', 'Fiat', 2006, 'abc1234')

# com o uso do argumento nomeado podemos inverter a ordem: 
definir_carro(marca='Fiat', ano= 2006, nome='Palio', placa= 'abc1234')

# usando um dicionario para nomear argumentos: 
definir_carro(**{'ano': 2006, 'nome': 'Palio', 'marca': 'Fiat', 'placa': 'abc1234'})

## *Args e **Kwargs: quando são passadados como parâmetro significa que podemos passar uma lista com um numero de itens indefinidos 
## e podemos usar um dicionário com o numero de itens indefinidos respectivamente. 

def exibir_poema(data, *args, **kwargs):
    data_e_hora = data
    texto = '\n'.join(args)
    metadados = '\n'.join([f'{chave}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_e_hora}\n{texto}\n\n{metadados}'
    print(mensagem)


#forma 1 de fazer:

listaa = ['Era dia', 'mas em mim', 'era noite', 'era escuro como a madrugada',]
dicio = {'autor': 'Robert', 'ano': 2023}

exibir_poema('Quarta, 27 de setembro de 2023\n', *listaa, **dicio)

# forma 2 de fazer: ele toma tudo o que vem depois do primeiro argumento como um item da lista e tudo o que está nomeado como um item 
# de um dicionário

exibir_poema('Quarta, 27 de setembro de 2023\n', 'Era dia', 'mas em mim', 'era noite',
              'era escuro como a madrugada', autor='Robert', ano = 2023)

