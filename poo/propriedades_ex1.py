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