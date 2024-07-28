"""
Esse é um script contendo todos os desafios do curso  python fundamentals da DIO - 27/07/24
"""
# desafio 1

# def soma_tupla(tupla):
#     return sum(tupla)
#
#
# if __name__ == "__main__":
#     entrada = input()
#     # No "TODO", abaixo: Defina tupla para receber os números inteiros:
#     elementos = tuple(map(int, entrada.split()))
#     print(elementos)
#     resultado = soma_tupla(elementos)
#     print(f"A soma dos elementos da tupla é: {resultado}")

# desafio 2

# TODO: Crie uma função 'elementos_comuns' que receba duas listas de números inteiros separados por espaço:


# def elementos_comuns(lista_1, lista_2):
#     set_1 = set(map(int, lista_1))
#     set_2 = set(map(int, lista_2))
#
#     return list(set_1.intersection(set_2))
#
#
# # Leitura das listas
# lista_1 = input().split()
# lista_2 = input().split()
#
# # Verifica se todas os elementos das listas podem ser convertidos para inteiros
# if all(item.isdigit() for item in lista_1) and all(item.isdigit() for item in lista_2):
#     comuns = elementos_comuns(lista_1, lista_2)
#     print(f"Elementos comuns às duas listas: {comuns}")
# else:
#     print("Entrada inválida.")

# desafio 3

def contar_caracteres(string):
    # TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}
    # TODO: Itere através de cada caractere na string string.
    for char in string:
    # TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1

    return contador


# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)

