class Cachorro:
    def __init__(self, nome, cor, acordado = True) -> None: #o __init__ é executado sempre que a classe é estanciada. é o primeiro metodo a ser executado
        print("inicializando a classe ... ")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("removendo a instancia da classe...")  # o __del__ é um método destrutor e só é executado ao final do programa independente da ordem

    def latir(self):
        print("au au!")


## reparar o __del__ 

# cachorro_1 = Cachorro('Toby', 'preto e branco', False)
# cachorro_1.latir()

# print(cachorro_1)

# print('alo globo')
# print('alo globo')


# print('alo globo')
# print('alo globo')
# print('alo globo')

# note que o escript  * <codigo> * retorna: 

# inicializando a classe ... 
# au au!
# <__main__.Cachorro object at 0x7fb619b30640>
# alo globo
# alo globo
# alo globo
# alo globo
# alo globo
# removendo a instancia da classe...

# é possível forçar o del a excluir o objeto antes 

cachorro_1 = Cachorro('Toby', 'preto e branco', False)
cachorro_1.latir()

print(cachorro_1)

print('alo globo')
print('alo globo')

del cachorro_1
cachorro_1.latir()

print('alo globo')
print('alo globo')
print('alo globo')