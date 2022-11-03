nome = "Vinicius"
idade = 22
profissao = "Chefe de divisão" 
linguagem = "Python"
PI = 3.14159

#forma %

print("Nome: %s , Idade: %d" % (nome, idade))

#forma format

print("Nome: {1} , Idade: {0}".format(idade, nome))

#forma f-string

print(f"Nome: {nome}, Idade: {idade}")
print(f"Valor de PI: {PI:.2f}") 