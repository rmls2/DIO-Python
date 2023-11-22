
## funçoes sã objetos de primeira ordem, dessa forma podem receber como argumenbto funções


# def party():
#     print("Estou de fora =[")

#     def start_party():
#         entrada = input('Vai para a festa? ')

#         if entrada == 's':
#             return "Estamos dentro! Uhullll!"
#         else:
#             return "deu ruim :/"

#     def finish_party():
#         return "A festa acabou! =["

#     print(start_party())
#     print(finish_party())

# "Criador" de funções de potência


def cria_potencia(x):
    def potencia(num):
        def encremento(num2):
            return x ** num + num2
        return encremento
    return potencia

cria_potencia(2)
cria_potencia(3)

# Resultado
print(cria_potencia(2)(2)(1))
print(cria_potencia(3)(2)(1))