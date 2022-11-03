entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

soma = diametro1 + diametro2
resultado = distancia / soma

print(f"{resultado:.2f}")