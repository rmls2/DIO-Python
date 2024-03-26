class Foo:
    def __init__(self, x) -> None:
        self._x = x 

    @property     ##o property retorna valor, é uma forma de acesso ao atributo x
    def x(self):
        return self._x or 0 
    @x.setter       ## não retorna valor. Para atribuir valor para o property é por meio do setter
    def x(self, value):
        self._x += value
    @x.deleter
    def x(self):
        # # pode se usar o del para deletar um atributo da maneira abaixo
        # print('deletando com sucesso o _x')
        # del self._x
        print('setando x para 0') ##essa é a forma "exclui o valor do atributo mas o conserva"
        self._x = 0   
    
foo = Foo(20)
print(foo.x)
foo.x = 10
print(foo.x)

del foo.x 
print(foo.x)
foo.x = 10
print(foo.x)

print('esse é o valor de x agora', foo.x)

# exemplo de uso de decorator, fora do contexto de classe.:

def decorator(funcao):
    def wrapper():
        print ("Estou antes da execução da função passada como argumento")
        funcao()
        print ("Estou depois da execução da função passada como argumento")

    return wrapper

def outra_funcao():
    print ("Sou um belo argumento!")

funcao_decorada = decorator(outra_funcao)
funcao_decorada()

## outro exemplo:

import time

# Define nosso decorator
def calcula_duracao(funcao):
    def wrapper():
        # Calcula o tempo de execução
        tempo_inicial = time.time()
        time.sleep(5)
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