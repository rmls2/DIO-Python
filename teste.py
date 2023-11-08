# x = {1 : "a", 2 :"b"}

# def alterax(a: dict) -> dict:

#     a.setdefault(3)

#     return a

# print(x)

# alterax(x)

# print(x)


# Definição da Função recebendo kwargs
def funcao(**kwargs):
    # Percorrendo argumento nomeados
    for chave in kwargs:
        print(f"Acessando Chave '{chave}', valor = {kwargs.get(chave)}")

regulagem = {'max': 10, 'meio': 5, 'min': 0}

funcao(**regulagem)

contatos = {
    'miller182@': {'nome': 'Robert', 'idade': 26},
    'karol@': {'nome': 'Karolyne', 'idade': 26},
    'gabghv@': {'nome': 'Gabriel', 'idade': 22},
    'bruno@': {'nome': 'Bruno', 'idade': 23} 
}

contatos.update({'miller182@': 'cara', 'karol@': 'muie'})


def imc(peso_kg, altura_em_metros):
    """ essa função calcula o imc de acordo com o peso"""
    return (peso_kg/altura_em_metros**2)


meu_imc = imc(100, 1.85)
print(meu_imc)
# help(imc)


x =10 

y = 11

def externa():
    x = 13
    print(x)
    print(f'valor de x = {x}')
    print(id(x))
    def interna():
        x = 13
        print(f'valor de x = {x}')
        print(id(x))
    interna()
x = 13
externa()
print(f'valor de x = {x}')
print(id(x))


lista = ['1','2','3','4', 5, '6']



print(x)

def testec():
    """ esse é um docstring"""

