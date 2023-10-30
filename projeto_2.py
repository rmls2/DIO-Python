import textwrap


def sacar(*,valor_saque, extrato: list, limite, limite_saques, saldo_conta, numero_saques_conta) -> tuple: # o * vai definir a função sacar com argumentos todos nomeados
    
    excedeu_saldo = valor_saque > saldo_conta

    excedeu_limite = valor_saque > limite

    excedeu_saques = numero_saques_conta >= limite_saques
    
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print('*'*50)
        print("\nOperação falhou! Número máximo de saques excedido.")
        print('*'*50)

    elif valor_saque > 0:
        saldo_conta -= valor_saque
        extrato.append(f"Saque: R$ {valor_saque:.2f}")
        numero_saques_conta += 1
        print('\nSaque realizado com sucesso!')

    else:
        print("\n\nOperação falhou! O valor informado é inválido.")

    return saldo_conta, extrato

def depositar(valor_deposito, extrato: list, saldo_conta, /) -> tuple: # / vai dizer que todos os argumentos são posicionais

    if valor_deposito > 0:
            saldo_conta += valor_deposito
            extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
            print('\nDepósito realizado com sucesso!')
    else:
        print("Operação falhou! O valor do depósito é invalido.")

    return saldo_conta, extrato

def extrato_(saldo_conta, /,*, extrato ): # / e * vai determinar que saldo_conta é posicional e extrato é argumento nomeado

    print("\n==================== EXTRATO =======================")

    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            if item:
                print(item)
    print(f"\nSaldo: R$ {saldo_conta:.2f}")
    print("====================================================")

def cadastrar_usuario(usuarios: list) -> dict:
    cpf = input("\nDigite o cpf do usuário: ")

    usuario = filtrar_usuario(cpf, usuarios)
    # verifica se o cpf ja está cadastrado
    
    if usuario:
        print('\n------------------------------------------')
        print('Operação inválida! Usuário ja cadastrado!')
        print('------------------------------------------')

        return None

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    print('\nUsuário cadastrado com sucesso!')
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
 
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\nInforme o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

def listar_usuarios(usuarios_banco):
    print('\n=============== Usuários do Banco ==================')
    for usuario in usuarios_banco:
        linha = f"""
            Nome: {usuario['nome']}
            Data de nascimento: {usuario['data_nascimento']}
        """
    if usuarios_banco:
        print(textwrap.dedent(linha))
    else:
        print('\n\tAinda não há usuários cadastrados!')

def menu():
    menu = """
===================== MENU =========================
[d] Depositar
[s] Sacar
[e] Extrato
[v] Vincular conta
[c] Cadastrar usuario
[l] Listar usuários
[q] Sair

=> """
    return input(menu)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def main():

    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    saldo_conta = 0
    limite_conta = 500
    extrato_conta = []
    numero_saques_conta = 0
    usuarios_banco = []
    contas_cadastradas = []
    contador = 0 

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("\nInforme o valor do depósito: "))
            saldo_conta, extrato_conta = depositar(valor, extrato_conta, saldo_conta)
            
        elif opcao == 's':
            valor = float(input("\nInforme o valor do saque: "))
            saldo_conta, extrato_conta = sacar(valor_saque=valor, extrato=extrato_conta, limite=limite_conta, limite_saques=LIMITE_SAQUES, saldo_conta= saldo_conta, numero_saques_conta= numero_saques_conta)

        elif opcao == 'e':
            extrato_(saldo_conta, extrato=extrato_conta)

        elif opcao == 'c':
            cadastrar_usuario(usuarios_banco)

        elif opcao == 'v':
            numero_conta = contador + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios_banco)

            if conta:
                contas_cadastradas.append(conta)

        elif opcao == 'l':
            listar_usuarios(usuarios_banco)

                
        elif opcao == 'q':
            print('\n====================================================')
            print('\nAgradecemos o seu contato. Tenha um bom dia!\n')
            break
        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")


main()





