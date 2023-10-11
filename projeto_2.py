## parte 1

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo_conta = 0
limite_conta = 500
extrato_conta = []
numero_saques_conta = 0
LIMITE_SAQUES = 3

def sacar(valor_saque, extrato, limite, limite_saques) -> tuple:
    global saldo_conta, numero_saques_conta

    excedeu_saldo = valor_saque > saldo_conta

    excedeu_limite = valor_saque > limite

    excedeu_saques = numero_saques_conta >= limite_saques
    
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor_saque > 0:
        saldo_conta -= valor_saque
        extrato.append(f"Saque: R$ {valor_saque:.2f}")
        numero_saques_conta += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return extrato, valor_saque

def depositar(valor_deposito, extrato: list) -> tuple:
    global saldo_conta

    if valor_deposito > 0:
            saldo_conta += valor_deposito
            extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
    else:
        print("Operação falhou! O valor do depósito é invalido.")

    return saldo_conta, extrato

def extrato_(saldo_conta, /,*, extrato ):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo_conta:.2f}")
    print("==========================================")

## parte 2 

def criar_usuario(nome, data_nascimento, cpf , endereço):
    pass

def criar_conta_corrente(): 
    pass
    
# while True:
#     pass


saldo_conta = 800
limite_conta = 500

print(saldo_conta, extrato_conta)

depositar(510, extrato_conta)
sacar(valor_saque = 50, extrato= extrato_conta, limite = limite_conta, limite_saques = LIMITE_SAQUES)

extrato_(saldo_conta, extrato = extrato_conta)