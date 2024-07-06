from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

class Conta: 

    def __init__(self,numero, cliente: object) -> None:
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
            self._saldo -=valor
            print("\n === Saque realizado com sucesso! ===")
            return True 
        else:
            print('\n @@@ Operação falhou, você não tem saldo suficiente! @@@')
            return False

    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
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

    @property
    def contas(self):
        return self._contas
    
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

    def __init__(self,numero, cliente: object, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False    
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return super().nova_conta(cliente, numero)

    
    def __str__(self) -> str:
        return f"""\ 
                Agência:\t{self.agencia}
                C/C:\t\t{self.numero}
                Titular:\t{self.cliente.nome}
                """

def filtrar_cliente(clientes: list, cpf_cliente)-> list:
    cliente_cadastrado = [cliente for cliente in clientes if cliente.cpf == cpf_cliente]
    return cliente_cadastrado

def filtrar_conta(contas: list, numero_conta) -> list:
    conta_cadastrada = [conta_banco for conta_banco in contas if conta_banco.numero == numero_conta ]
    return conta_cadastrada

def novo_usuario(clientes: list) -> None:
    endereco_ciente = input("Digite o endereço do cliente: ")
    cpf_cliente = input("Digite o cpf do cliente: ")
    nome_cliente = input("Digite o nome do cliente: ")
    data_nascimento_cliente = input("Digite a data de nascimento do cliente: ")

    usuario = PessoaFisica(endereco_ciente, cpf_cliente, nome_cliente, data_nascimento_cliente)
    if usuario in clientes:
        print("Cliente já cadastrado!")
        usuario = None
        return None
    clientes.append(usuario)

    print("\n=== Cliente criado com sucesso! ===")

def nova_conta(contas: list, clientes: list):
    cpf_cliente = input("Digite o seu cpf: ")
    cliente_cadastrado = filtrar_cliente(clientes=clientes, cpf_cliente=cpf_cliente)

    if not cliente_cadastrado:
        print("Cliente ainda não cadastrado! É preciso realizar o cadastro antes de criar uma conta")
        return None 
    
    cliente = cliente_cadastrado[0] 
    numero_conta = input("Digite o número da conta: ")
    conta_cadastrada = filtrar_conta(contas=contas, numero_conta=numero_conta)

    if conta_cadastrada:
        print("Essa Conta já existe!")

    nova_conta = ContaCorrente.nova_conta(numero=numero_conta, cliente=cliente)
    cliente.adcionar_conta(nova_conta)
    contas.append(nova_conta)
    
    print("\n=== Conta criada com sucesso! ===")


def depositar(clientes: list, contas: list, valor_deposito: float) -> None:
    cpf_cliente = input("Digite o seu cpf: ")
    cliente_cadastrado = filtrar_cliente(clientes=clientes, cpf_cliente=cpf_cliente)

    if not cliente_cadastrado:
        print("Você não cliente do banco! Realize seu cadasto")
        return None
    
    numero_conta = input("Digite o número da sua conta: ")
    conta_cadastrada = filtrar_conta(contas=contas, numero_conta=numero_conta)

    if not conta_cadastrada:
        print("Apesar de ser cliente, você não possui uma conta! Crie uma conta primeiro")
        return None

    Deposito(valor_deposito).registrar(conta_cadastrada[0])

    
def sacar(clientes: list, contas: list, valor_saque: float):
    cpf_cliente = input("Digite o seu cpf: ")
    cliente_cadastrado = filtrar_cliente(clientes=clientes, cpf_cliente=cpf_cliente)

    if not cliente_cadastrado:
        print("Você não cliente do banco! Realize seu cadasto")
        return None
    
    numero_conta = input("Digite o número da sua conta: ")
    conta_cadastrada = filtrar_conta(contas=contas, numero_conta=numero_conta)[0]

    if not conta_cadastrada:
        ("Cliente não possui uma conta! Crie uma conta no nosso banco para poder realizar um saque!")
        return None
    Saque(valor_saque).registrar(conta_cadastrada)

def extrato(clientes: list):
    cpf_cliente = input("Informe o CPF do cliente: ")
    cliente_cadastrado = filtrar_cliente(clientes=clientes, cpf_cliente=cpf_cliente)[0]

    if not cliente_cadastrado:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    numero_conta = input("Por favor, digite o número da sua conta: ")
    conta_extrato = [conta for conta in cliente_cadastrado.contas if numero_conta == conta.numero][0]
    
    if not conta_extrato:
        print("\n@@@ Conta não encontrada! @@@")
        return

    print("\n================ EXTRATO ================")
    transacoes = conta_extrato.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta_extrato.saldo:.2f}")
    print("==========================================")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

    

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
    clientes_banco = []
    contas_banco = []

    while True:
        opcao = menu()
        match opcao:
            case "d":
                deposito = float(input("Digite o valor do deposito: "))
                depositar(clientes=clientes_banco, contas=contas_banco, valor_deposito=deposito)
            case "s":
                saque = float(input("Digite o valor do saque: "))
                sacar(clientes_banco, contas_banco, saque)
            case "e":
                extrato(clientes_banco)
            case "nc":
                nova_conta(contas=contas_banco, clientes=clientes_banco)
            case "lc":
                listar_contas(contas_banco)
            case "nu":
                novo_usuario(clientes=clientes_banco)
            case "q":
                break

    
main()