menu = """

Olá, seja bem-vindo!
Qual operação deseja realizar?

[1] Saque
[2] Depósito
[3] Ver Extrato
[4] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print(
            """
             [Saque]
            ---------
            """
        )
        saque = float(input("Qual valor deseja sacar? "))
        if saque > 0 and saque <= saldo and numero_saques < LIMITE_SAQUES and saque <= limite:
            print("\nSaque realizado com sucesso!")
            saldo -= saque
            extrato += f"\nSaque no valor de R${saque:.2f}"
            numero_saques += 1
        else:
            if saque > saldo:
                print("\nNão há saldo o suficiente para realizar essa operação!")
                print("Realize um depósito em sua conta!")
            elif saque > limite:
                print("\nAcima do limite!!")
                print("Seu valor disponível para saque é de R$500 por operação.")
            elif numero_saques == LIMITE_SAQUES:
                print("\nLimite de saques diários foi atingido. 3/3")
                print("Para efetuar mais saques, retorne amanhã.")

    elif opcao == "2":
        print(
            """
            [Depósito]
            ----------
            """
        )
        deposito = float(input("Qual valor deseja depositar? "))
        if deposito > 0:
          saldo += deposito
          print("\nDepósito realizado com sucesso!")
          extrato += f"\nDepósito no valor de R${deposito:.2f}"
        else:
            print("Erro no sistema!")
            print("Verifique o valor a ser depositado e tente novamente.")

    elif opcao == "3":
        print(
            """
             [Extrato]
             ---------
             """
        )
        print("Não foi feita nenhuma operação.") if extrato == "" else print(extrato)
        print("-----------------------------")
        print(f"\nSaldo da conta: R${saldo:.2f}")

    elif opcao == "4":
        print(
            """
             Obrigado por escolher o nosso banco.
             Volte Sempre!
             
             """
        )
        break

    else:
        print(
            """
             Operação inválida!
             Por favor, selecione novamente a operação desejada.
             
             """
        )
