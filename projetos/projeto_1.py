
menu = """
    Bem vindo(a) ao Banco de Pernambuco
    Selecione uma das opções abaixo:

    [1] Depósito
    [2] Sacar
    [3] Extrato
    [4] Sair

    => """

saldo = 0
limite = 500
extrato_depositos = "Depositos: "
extrato_saques = "Saques: "
numero_saques = 0
extrato = ''
LIMITE_SAQUES = 3 


while True:

    opcao = input(menu)

    if opcao == "1":
        print("\n    Depósito \n")

        valor_deposito = float(input("    Digite quanto você quer depositar: "))
        saldo += valor_deposito
        extrato_depositos += f"R${valor_deposito:.2f} "


    elif opcao == "2":
        print("\n    Sacar \n")

        valor_saque = float(input('    Digite o quanto você quer sacar: '))
        if LIMITE_SAQUES == 0 or valor_saque > saldo:
            if valor_saque > saldo:
                print("\n    Saldo insuficiente!")
            break
        else: 
            saldo -= valor_saque
            LIMITE_SAQUES-=1
            extrato_saques += f"R${valor_saque:.2f} "

    elif opcao == "3":
        if extrato == '':
            print("\n    Não foram realizadas movimentações.")
        print(extrato)
        break    
    elif opcao == "4":
        print("Tenha um bom dia!")
        break

    else:
        print('Operação inválida. Por favor, selecione novamente a operação desejada')
    extrato = f"""\n    ###### Extrato #######\n\n    {extrato_saques}\n    {extrato_depositos}\n    Saldo: R${saldo: .2f}"""


# print(extrato_depositos)
# print(extrato_saques)
# print(extrato)