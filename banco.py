from time import sleep

titular = ()

saldo = []

historico = []

print(41*"=")
print("Seja bem-vindo ao Sistema Bancário da JWC")
print(41*"=")
print("")

titular = input("Digite o nome do titular da conta: ")
print("")

while not all(palavra.isalpha() for palavra in titular.split()):
    titular = input("Nome inválido! Digite o nome do titular da conta (Apenas letras): ")

saldo = input("Digite a quantia inicial para depósito: R$")

while True:
    try:
        saldo = float(saldo)
        if saldo < 1:
            raise ValueError
        
        break
    except ValueError:
        saldo = input("Valor inválido! Digite uma quantia inicial positiva numérica: R$")

while True:
    print(25*"=")
    print("Depositar (1)")
    print(25*"=")
    print("Sacar (2)")
    print(25*"=")
    print("Consultar Saldo (3)")
    print(25*"=")
    print("Consultar Histórico (4)")
    print(25*"=")
    print("Sair (5)")
    print("")

    operacao = input("Escolha a operação que deseja realizar (Nº): ")

    while True:
        try:
            operacao = int(operacao)
            if operacao < 1 or operacao >= 6:
                raise ValueError

            break
        except ValueError:
            operacao = input("Operação inválida! Digite apenas o número da operação que deseja realizar (Nº): ")
            
    print("")

    if operacao == 1:
        deposito = input("Digite a quantia que deseja depositar: R$")

        while True:
            try:
                deposito = float(deposito)
                if deposito < 1:
                    raise ValueError

                break
            except ValueError:
                deposito = input("Valor inválido! Digite uma quantia positiva que deseja depositar: R$")

        print("")

        confirmacao_deposito = False
        confirm_deposito_input = input(f"Será realizado um depósito de: R${deposito}. Deseja confirmar? (1-Sim, 2-Não) ")

        while True:
            try:
                confirm_deposito_input = int(confirm_deposito_input)
                if confirm_deposito_input < 1 or confirm_deposito_input > 2:
                    raise ValueError

                break
            except ValueError:
                confirm_deposito_input = input(f"Opção inválida! Digite apenas 1 para SIM, ou 2 para NÃO. Deseja confirmar o depósito? ")

        print("")

        if confirm_deposito_input == 1:
            confirmacao_deposito = True

        else:
            confirmacao_deposito = False

        if confirmacao_deposito == True:
            saldo += deposito
            historico.append(f"Depósito de R${deposito} realizado.")
            print(32*"-")
            print("Depósito realizado com sucesso!")
            print(32*"-")
            print("")
            sleep(3)

        else:
            print(37*"-")
            print("Operação cancelada. Retornando...")
            print(37*"-")
            print("")
            sleep(3)

    if operacao == 2:
        saque = input("Digite a quantia que deseja sacar: R$")

        while True:
            try:
                saque = float(saque)
                if saque < 1:
                    raise ValueError

                break
            except ValueError:
                saque = input("Valor inválido! Digite uma quantia positiva a ser sacada: R$")

        print("")

        confirmacao_saque = False
        confirm_saque_input = input(f"Será realizado um saque de: R${saque}. Deseja confirmar? (1-Sim, 2-Não) ")

        while True:
            try:
                confirm_saque_input = int(confirm_saque_input)
                if confirm_saque_input < 1 or confirm_saque_input > 2:
                    raise ValueError

                break
            except ValueError:
                confirm_saque_input = input("Opção inválida! Digite 1 para SIM, ou 2 para NÃO. Deseja confirmar o saque? ")

        print("")

        if confirm_saque_input == 1:
            confirmacao_saque = True

        else:
            confirmacao_saque = False

        if confirmacao_saque == True:
            
            if saldo >= saque:
                saldo -= saque
                historico.append(f"Saque de R${saque} realizado.")
                print(30*"-")
                print("Saque realizado com sucesso!")
                print(30*"-")
                print("")
                sleep(3)

            else:
                print(50*"-")
                print("Saldo da conta insuficiente para realizar um saque!")
                print(50*"-")
                print("")
                sleep(3)

        else:
            print(37*"-")
            print("Operação cancelada. Retornando...")
            print(37*"-")
            print("")
            sleep(3)

    if operacao == 3:
        print(42*"-")
        print(f"Nome do titular da conta: {titular}")
        print(f"O saldo atual da sua conta é de: R${saldo}")
        print(42*"-")
        print("")
        sleep(4)

    if operacao == 4:

        if len(historico) == 0:
            print(30*"-")
            print("Histórico de transações vazio!")
            print(30*"-")
            print("")
            sleep(3)

        else:
            print(30*"=")
            print("Histórico de transações atual:")

            for i in range(0, len(historico)):
                print(20*"-")
                print(f"{i + 1} - {historico[i]}")

            print(30*"=")
            print("")
            sleep(3 + len(historico))

    if operacao == 5:
        print(45*"-")
        print("Obrigado por usar os nossos serviços! Finalizando...")
        print(45*"-")
        sleep(1)
        break
