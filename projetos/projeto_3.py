from abc import ABC, abstractmethod


class Conta: 

    def __init__(self,numero, cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico() 

    @property
    def saldo(self):
        return self._saldo

    @classmethod
    def nova_conta(cls, cliente: object, numero):

        return cls(numero, cliente)
    
    def sacar(self):
        pass

    def depoositar(self):
        pass

class Transacao(ABC):

    @abstractmethod
    def registrar(Conta: Conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float) -> None:
        self._valor = valor

class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
        
class Cliente:
    def __init__(self, endereco, contas: list) -> None:
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(conta: Conta, transacao: Transacao):
        pass

    def adcionar_conta(conta: Conta):
        pass

class PessoaFisica(Cliente):

    def __init__(self, endereco, contas: list, cpf, nome, data_nascimento) -> None:
        super().__init__(endereco, contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Historico:
    def __init__(self, historico:list) -> None:
        self.historico = historico  

    def adcionar_transacao(transacao: Transacao):
        pass

class ContaCorrente(Conta):
    def __init__(self, limite, limite_saques):
        self._limite = limite
        self._limite_saques = limite_saques
    
