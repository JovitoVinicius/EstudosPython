valores = input().split()

CONSUMO_LITRO = 12

tempo = int(valores[0])
velocidade_media = int(valores[1])

resultado = (velocidade_media * tempo) / CONSUMO_LITRO

print(f"{resultado:.3f}")