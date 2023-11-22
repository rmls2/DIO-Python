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
