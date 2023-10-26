def sacar(*,valor_saque, extrato: list, limite, limite_saques, saldo_conta, numero_saques_conta) -> tuple: # o * vai definir a função sacar com argumentos todos nomeados
    
    excedeu_saldo = valor_saque > saldo_conta

    excedeu_limite = valor_saque > limite

    excedeu_saques = numero_saques_conta >= limite_saques
    
    
    if excedeu_saldo:
        print('\n')
        print('*'*50)
        print("Operação falhou! Você não tem saldo suficiente.")
        print('*'*50)
    elif excedeu_limite:
        print('*'*50)
        print("Operação falhou! O valor do saque excede o limite.")
        print('*'*50)
    elif excedeu_saques:
        print('*'*50)
        print("\nOperação falhou! Número máximo de saques excedido.")
        print('*'*50)

    elif valor_saque > 0:
        saldo_conta -= valor_saque
        extrato.append(f"Saque: R$ {valor_saque:.2f}")
        numero_saques_conta += 1

    else:
        print("\n\nOperação falhou! O valor informado é inválido.")

    return saldo_conta, extrato

def depositar(valor_deposito, extrato: list, saldo_conta, /) -> tuple: # / vai dizer que todos os argumentos são posicionais

    if valor_deposito > 0:
            saldo_conta += valor_deposito
            extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
    else:
        print("Operação falhou! O valor do depósito é invalido.")

    return saldo_conta, extrato

def extrato_(saldo_conta, /,*, extrato ): # / e * vai determinar que saldo_conta é posicional e extrato é argumento nomeado

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo_conta:.2f}")
    print("==========================================")

## parte 2 

def cadastrar_usuario(nome: str, data_nascimento: str, cpf: str , endereço: str) -> dict:
    dados_do_usuarios = dict()
    global usuarios_banco #lista de usuarios

    usuario = filtrar_usuario(cpf, usuarios_banco)
    # verifica se o cpf ja está cadastrado
    
    if usuario:
         # caso não possua o cadastro, o cadastro é feito e seus dados aramazenados no dicionario
        dados_do_usuarios['cpf'] = cpf
        dados_do_usuarios['nome'] = nome
        dados_do_usuarios['data de nascimento'] = data_nascimento
        dados_do_usuarios['endereço'] = endereço
        usuarios_banco.append(dados_do_usuarios)

    else:
        print('Operação inválida! Usuário ja cadastrado')
       
    
def criar_conta(agencia, numero_conta, usuarios, contas_cadastradas, cpf, nome_do_usuario):
    
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        contas_cadastradas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": nome_do_usuario})

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

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

def listar_usuarios(usuarios_banco):
    print('\n***** Usuários do Banco *****')
    for usuario in usuarios_banco:
        linha = f"""\
            Nome: \t {usuario['nome']}
            Data de nascimento: \t {usuario['data de nascimento']}

        """
        print('='*50)
        print(linha)

######################################################################################################################

def menu():
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
            valor = float(input("Informe o valor do depósito: "))
            saldo_conta, extrato_conta = depositar(valor, extrato_conta, saldo_conta)
            
        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))
            saldo_conta, extrato_conta = sacar(valor_saque=valor, extrato=extrato_conta, limite=limite_conta, limite_saques=LIMITE_SAQUES, saldo_conta= saldo_conta, numero_saques_conta= numero_saques_conta)

        elif opcao == 'e':
            extrato_(saldo_conta, extrato=extrato_conta)

        elif opcao == 'c':
            nome = input('Digite o nome do usuário: ')
            data_nascimento = input('Digite a data de nascimento (dd/mm/aaaa): ') 
            cpf = input('Digite seu CPF (apenas numeros): ') 
            endereço = input('Digite seu endereço (<rua>, <numero da casa>, <bairro>- <cidade>/<estado>: ')  
            cadastrar_usuario(nome, data_nascimento, cpf, endereço)

        elif opcao == 'v':
            cpf = input("Digite o CPF do usuário: ")
            nome_do_usuario = input("Digite o nome do usuário: ")
            numero_conta = contador + 1

            criar_conta(AGENCIA, numero_conta, usuarios_banco, contas_cadastradas, cpf, nome_do_usuario )

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


main()





