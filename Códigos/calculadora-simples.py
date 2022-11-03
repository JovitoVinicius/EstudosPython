#Funções da calculadora

def soma(x, y):
    sum = x + y
    return sum

def subtracao(x, y):
    sub = x - y
    return sub

def divisao(x, y):
    div = x / y
    return div

def multiplicacao(x, y):
    mult = x * y
    return mult

def potenciacao(x, y):
    pot = x ** y
    return pot

def home(): #Menu
    print("+----------------------------------------+")
    print("|Calculadora Simples - by:Vinicius Jovito|")
    print("|                                        |")
    print("| 1 - Soma                               |")
    print("| 2 - Subtração                          |")
    print("| 3 - Divisão                            |")
    print("| 4 - Multiplicação                      |")
    print("| 5 - Potenciação                        |")
    print("+----------------------------------------+")
    return

home() #printa a tela de menu
opcao = int(input("Digite uma opção: ")) #recebe a opção desejada pelo usuário

while(opcao!=1 and opcao!=2 and opcao!=3 and opcao!=4 and opcao!=5): #validador de opção inválida
    print("\nDigite um valor valido!")
    opcao = int(input("Digite uma opção: "))


# Soma
if opcao == 1:
    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
    print("Resultado: ", soma(x, y))            

# Subtração
elif opcao == 2:
    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
    print("Resultado: ", subtracao(x, y))

# Divisão
elif opcao == 3:
    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
    while y == 0:
        print("O denominador não pode conter o valor 0, favor escolher outro valor para o denominador")
        y = int(input("Digite o segundo valor: "))
        
    print("Resultado: ", divisao(x, y))

# Multiplicação
elif opcao == 4:
    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
    print("Resultado: ", multiplicacao(x, y))

# Potenciação
elif opcao == 5:
    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
    print("Resultado: ", potenciacao(x, y))



