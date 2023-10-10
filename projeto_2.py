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

def sacar(valor_saque, extrato, limite, limite_saques):
    global saldo_conta, numero_saques_conta

    excedeu_saldo = valor_saque > saldo_conta

    excedeu_limite = valor_saque > limite

    excedeu_saques = numero_saques_conta >= limite_saques
    
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo_conta suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor_saque do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor_saque > 0:
        saldo_conta -= valor_saque
        extrato.append(f"Saque: R$ {valor_saque:.2f}")
        numero_saques_conta += 1

        return extrato, valor_saque

    else:
        print("Operação falhou! O valor_saque informado é inválido.")

def depositar(saldo_conta, valor_saque, extrato):
    pass

def extrato_(saldo_conta, *, extrato = 'extrato'):
    pass

def criar_usuario(nome, data_nascimento, cpf , endereço):
    pass

def criar_conta_corrente(): 
    pass
    
# while True:
#     pass


saldo_conta = 800

kwargs = {'valor_saque': 10, 'extrato': extrato_conta,'limite': limite_conta, 'limite_saques': LIMITE_SAQUES}
x = sacar(**kwargs)
print(x)
kwargs = {'valor_saque': 15, 'extrato': extrato_conta,'limite': limite_conta, 'limite_saques': LIMITE_SAQUES}
x = sacar(**kwargs)
print(x)
kwargs = {'valor_saque': 5, 'extrato': extrato_conta,'limite': limite_conta, 'limite_saques': LIMITE_SAQUES}
x = sacar(**kwargs)
print(x)
kwargs = {'valor_saque': 5, 'extrato': extrato_conta,'limite': limite_conta, 'limite_saques': LIMITE_SAQUES}
x = sacar(**kwargs)
print(x)




