""" class Editora:
    def __init__(self, autores, nro_publicacao) -> None:
        self.autores = autores
        self.nro_publicacao = nro_publicacao

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {", ".join([f"{chave}: {valor}" for chave, valor in self.__dict__.items()])}'

class Livro(Editora):
    def __init__(self, numero_paginas, **kw) -> None:
        self.numero_paginas = numero_paginas
        super().__init__(**kw)
        
    def muda_pagina(self, numero_da_pagina):
        return numero_da_pagina


class Capitulo(Editora):
   def __init__(self, **kw) -> None:
       super().__init__(**kw)

class Subcapitulo(Capitulo, Livro):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

sub = Subcapitulo(autores='yuval', nro_publicacao=20, numero_paginas=200)
print(sub) """

# class Livro:
#     def __init__(self, numero_paginas, autor, assunto) -> None:
#         self.numero_paginas = numero_paginas
#         self.autor = autor
#         self.assunto = assunto

#     def __str__(self) -> str:
#         return f'{self.__class__.__name__}: {", ".join([f"{chave}: {valor}" for chave, valor in self.__dict__.items()])}'

#     def muda_pagina(self, numero_da_pagina):
#         return numero_da_pagina

# class Editora:
#     def __init__(self, autores, nro_publicacao) -> None:
#         self.autores = autores
#         self.nro_publicacao = nro_publicacao

# class Capitulo(Livro, Editora):
#     def __init__(self, numero_paginas, autor, assunto, autores, nro_publicacao) -> None:
#         Livro.__init__(self, numero_paginas, autor, assunto)
#         Editora.__init__(self, autores, nro_publicacao)

# livro = Livro(200, 'Yuval Hahari', 'história')
# cap = Capitulo(numero_paginas=20, autor='Yuval Hahari', assunto='A história da humanidade', autores=1, nro_publicacao=10)
# print(cap)



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

import time

# Define nosso decorator
def calcula_duracao(funcao):
    def wrapper():
        # Calcula o tempo de execução
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        # Formata a mensagem que será mostrada na tela
        print("[{funcao}] Tempo total de execução: {tempo_total}".format(
            funcao=funcao.__name__.upper(),
            tempo_total=str(tempo_final - tempo_inicial))
        )

    return wrapper

# Decora a função com o decorator
@calcula_duracao
def main():
    for n in range(0, 10000000):
        pass

# Executa a função main
main()
