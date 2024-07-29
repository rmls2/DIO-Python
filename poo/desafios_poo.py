# # desafio 1
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#
#     # TODO: Crie um método para retornar as informações formatas com Nome e Idade:
#     def apresentacao(self):
#         return f"Nome: {self.nome}, Idade: {self.idade}"
#
#
#
# # Entrada do usuário
# nome = input()
# idade = int(input())
#
# # TODO: Crie uma instância da pessoa:
# pessoa = Pessoa(nome, idade)
# # TODO: Chame o método para retornar as informações formatadas e imprima o resultado:
#
# pessoa.apresentacao()

# desafio 2

class ConversorTemperatura:
    @staticmethod
    def celsius_para_fahrenheit(grau_celsius):
        return grau_celsius * (9/5) + 32

# Entrada do usuário
celsius = float(input())

# TODO: Crie uma instância do conversor:
conversor = ConversorTemperatura()
fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)
