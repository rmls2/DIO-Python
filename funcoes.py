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

## *Args e **Kwargs: quando são passadados como parâmetro significa que podemos passar uma lista ou tupla com um numero de itens indefinidos 
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


def soma(a, b):
    return a+b 

def exibir_func(n1,n2, funcao):
    resultado = funcao(n1,n2)

    print(f'o resultado de {n1} + {n2 } = {resultado}')


exibir_func(2,3, soma)

## Variáveis locais e globais 

# variáveis locais: quando o bloco de código for executado, as alterações feitas na variáveis vai desaparecer após isso. 
# variáveis globais: as alterações feitas por um bloco de código de uma função vão continuar após a execução 
# para dizer que uma variável é global se usa o global na hora de declarar a variável dentro da função 
# obs: usar variáveis globais não é uma boa prática 

resultado = 5

print(resultado)

def multiplica(a,b):
    global resultado
    resultado += a*b
    return resultado

print(multiplica(5,8))

# note que ao usar resultado como uma variável global o valor referenciado por ela foi add por aquilo que estava função (o produto de a e b)

valor = 5 
print(multiplica(valor, 3))

#note que ao passar valor como parâmetro dessa função ela irá multiplica valor * 3 e somar a variável resultado, que agora é
# uma variável global armazena o resultado original (5 + (5*8)) e ao chamar multiplica (valor, 3) foi add (3*5) e por tanto o 
# valor final de resultado é 60  

# ao passar um variável de fora do escopo da função como argumento pra ela, a função pode alterar o seu valor 
# geralmente altera o valor da lista só. Mas variáveis numéricas só mudam durante a execução da função.

lista_teste = [1,3]

def add_elemento_lista(a, lista):
    lista.append(a)
    print(lista)

add_elemento_lista(4, lista_teste)