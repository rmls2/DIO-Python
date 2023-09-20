class Numero:
    def __init__(self) -> None:
        self.numero = 2

x = Numero()

y = Numero()

x = y #dois objetos nesse caso só oassam a serem 

if x is y:
    print('x é igual a y')

else: 
    print('não sao iguais otario')