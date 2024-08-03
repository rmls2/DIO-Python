# def elementos_comuns(lista_1, lista_2):
#     set_1 = set(map(int, lista_1.split()))
#     set_2 = set(map(int, lista_2.split()))
#
#     return list(set_1.intersection(set_2))
#
#
# x = elementos_comuns('1 2 3 4', '3 4 5 6')
# print(x)

# verifica se uma string pode ser convetida para um número
# print('a'.isdigit())

# def meu_decorador(funct):
#     def func_envelope(*args, **kwargs):
#         print("antes da alteração")
#         x = funct(*args, **kwargs)
#         print("depois da alteração")
#         return x
#
#     return func_envelope
#
#
# @meu_decorador
# def ola_mundo(nome):
#     print(f"Ola, mundo doido de {nome}")
#     return nome.upper()
#
#
# print(ola_mundo('robert'))
l = []
if l is []:
    print('ola')