from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

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
    
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente: object, numero):

        return cls(numero, cliente)
    
    def sacar(self, valor: float):
        excedeu_saldo = valor > self._saldo
        
        if valor <= 0:
            print('\n@@@ Operação não suportada! Valor informado é inválido. @@@')
            return False
        elif not excedeu_saldo:
            self.saldo =-valor
            print("\n === Saque realizado com sucesso! ===")
            return True 
        else:
            print('\n @@@ Operação falhou, você não tem saldo suficiente! @@@')
            return False

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(Conta: Conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta: Conta):
        if conta.depositar(self.valor):
            conta.historico.adcionar_transacao(self)
            

class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta: Conta):
        if conta.sacar(self.valor):
            conta.historico.adcionar_transacao(self)

         
class Cliente:
    def __init__(self, endereco: str) -> None:
        self._endereco = endereco
        self._contas = []
    @staticmethod
    def realizar_transacao(conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

    def adcionar_conta(self, conta: Conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):

    def __init__(self, endereco: str, cpf, nome, data_nascimento) -> None:
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Historico:
    def __init__(self) -> None:
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adcionar_transacao(self, transacao: Transacao):
        return self._transacoes.append(
            {
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class ContaCorrente(Conta):

    def __init__(self,numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False        


    
    def __str__(self) -> str:
        return f"""\ 
                Agência:\t{self.agencia}
                C/C:\t\t{self.numero}
                Titular:\t{self.cliente.nome}
                """

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()
        match opcao:
            case "d":
                pass
            case "s":
                pass
            case "e":
                pass
            case "nc":
                pass
            case "lc":
                pass
            case "nu":
                pass
            case "q":
                break

    
main()