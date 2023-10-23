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
    # caso não possua o cadastro, o cadastro é feito e seus dados aramazenados no dicionario
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

def inativar_conta(usuario: str, numero_da_conta: int):
    pergunta_conta = input('Deseja inativar esta conta? (s/n)\n')
    global contas_cadastradas

    while True:
        match pergunta_conta:
            case 's':
                for conta in contas_cadastradas:
                    if conta['proprietario da conta'] == usuario and conta['numero da conta'] == numero_da_conta:
                        contas_cadastradas.remove(conta)
                        print(f'a conta do {usuario} foi removida com sucesso.')
                break    
            case 'n':
                print("Ok. Obrigado por continuar conosco!\n")
                break
            case _:
                print('opção inválida!\n')
                break

def listar_usuarios():
    print('\nUsuários do Banco:')
    for usuario in usuarios_banco:
        print('-',usuario)

######################################################################################################################
        
saldo_conta = 0
limite_conta = 500
extrato_conta = []
numero_saques_conta = 0
LIMITE_SAQUES = 3
usuarios_banco = []
contas_cadastradas = []

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[v] Vincular conta
[c] Cadastrar usuario
[l] Listar usuários
[i] Inativar conta
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == 'd':
         valor = float(input("Informe o valor do depósito: "))
         depositar(valor, extrato_conta)
         
    elif opcao == 's':
        valor = float(input("Informe o valor do saque: "))
        sacar(valor_saque=valor, extrato=extrato_conta, limite=limite_conta, limite_saques=LIMITE_SAQUES)

    elif opcao == 'e':
        extrato_(saldo_conta, extrato=extrato_conta)

    elif opcao == 'c':
        nome = input('Digite o nome do usuário: ')
        data_nascimento = input('Digite a data de nascimento (dd/mm/aaaa): ') 
        cpf = input('Digite seu CPF (apenas numeros): ') 
        endereço = input('Digite seu endereço (<rua>, <numero da casa)/<estado>-<cidade>: ')  
        cadastrar_usuario(nome, data_nascimento, cpf, endereço)

    elif opcao == 'v':
        usuario = input('Digite o nome do usuário do banco: ') 
        cpf = input('Digite o CPF do usuário: ')
        criar_conta_corrente(usuario, cpf)

    elif opcao == 'l':
        listar_usuarios()

    elif opcao == 'i':
        print('Você digitou a opção de inativar conta.')
        continue_ = input('Deseja continuar? (s/n): ')

        if continue_ == 's':
            usuario = input('Digite o nome do usuario: ')
            numero_da_conta = int(input('Digite o numero da conta: '))
            inativar_conta(usuario, numero_da_conta)
        else:
            print('operação cancelada.')
            
    elif opcao == 'q':
        print('Agradecemos o seu contato. Tenha um bom dia!')
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")