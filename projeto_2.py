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
usuarios_banco = []
contas_cadastradas = []

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

def cadastrar_usuario(nome: str, data_nascimento: str, cpf: str , endereço: str) -> dict:
    dados_do_usuarios = dict()
    global usuarios_banco #lista de usuarios
    # verifica se o cpf ja está cadastrado
    for i in usuarios_banco:
        if i['cpf'] == cpf:
            print('Operação inválida! Usuário ja cadastrado')
            return dados_do_usuarios
    # caso não possua, o cadastro é feito e seus dados aramazenados no dicionario
    dados_do_usuarios['cpf'] = cpf
    dados_do_usuarios['nome'] = nome
    dados_do_usuarios['data de nascimento'] = data_nascimento
    dados_do_usuarios['endereço'] = endereço

    usuarios_banco.append(dados_do_usuarios)
    
    return dados_do_usuarios

def criar_conta_corrente(usuario: str, cpf:str) -> dict: 
    NUMERO_AGENCIA = '0001'
    conta = dict()
    global contas_cadastradas #lista de contas
    # procurar na lista de usuarios pelo cpf do usuario e o nome do usuaruio
    # é impossível criar uma conta sem um usuário
    for cliente in usuarios_banco:
        if cliente['cpf'] == cpf and cliente['nome'] == usuario:
            conta['proprietario da conta'] = cliente['nome']
            conta['numero da conta'] = len(contas_cadastradas)+1
            conta['numero da agencia'] = NUMERO_AGENCIA

            contas_cadastradas.append(conta)
            return conta
    
        else:
            print(
                '''Usuário ainda não cadastrado ou nome e/ou cpf invalido!\nPor favor, cadastre o usuário antes de criar uma conta ou revise o nome e o cpf do usuário''')
            return conta

    
# while True:
#     pass

## parte 3: criar as funções complementares


cadastrar_usuario('robert', '12-25-23', '1223344', 'rua caraca')
print(usuarios_banco)
criar_conta_corrente('robert','223344')
print(contas_cadastradas)