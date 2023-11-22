class Conta:
    def __init__(self, numero, saldo) -> None:
        self._numero = numero
        self._saldo = saldo
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, novo_numero):
        if novo_numero >= 0:
            self._numero = novo_numero
        else:
            print("numero invalido. Coloque um numero maior que 0")

    @numero.deleter
    def numero(self):
        self._numero = 0
        print('setando numero = 0')
        

conta = Conta(123, 500.00)

print(conta.numero)
conta.numero = -122
print('agora conta vai ter: ', conta.numero)
del conta.numero

print(conta.numero)