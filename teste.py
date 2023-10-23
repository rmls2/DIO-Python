listaa = ['Era dia', 'mas em mim', 'era noite', 'era escuro como a madrugada',]
dicio = {'autor': 'Robert', 'ano': 2023}

def exibir_poema(data, *args, **kwargs):
    data_e_hora = data
    texto = '\n'.join(args)
    metadados = '\n'.join([f'{chave}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_e_hora}\n{texto}\n\n{metadados}'
    print(mensagem)


x = [10]

def teste(a: list):
    a.append(1)

    return a

print(x)

y = teste(x)

print(y)
print(x)
