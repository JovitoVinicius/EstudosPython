valor = 500.0
opcao = int(input("Digite uma opção: | [1] Sacar | [2]Extrato: "))

if opcao == 1:
    saque = float(input("Quanto deseja retirar? "))
    
    
    if saque > valor:
        print("Saldo Insuficiente!")

    status = "Sucesso" if valor >= saque else "Falha"
    print( f"{status} ao realizar o saque!")
    valor -= saque

elif opcao == 2:
    print("Exibindo extrato...")
    print("Valor atual é: ",valor)
else:
    print("Opção Inválida")

