nome = input("Escreva seu Primeiro nome: ")


print("Seu nome em caixa alta: ", nome.upper())
print("Seu nome com inicial Maiúscula: ", nome.title())
print("Seu nome em letra Minúscula:", nome.lower())

print("Seu nome centralizado com caracteres nas pontas: ", nome.center(14, "|"))
print("Seu nome com letras separadas por pontos: ", ".".join(nome))