# ler o peso de 5 pessoas e no final falar qual foi o maior e menor
'''
print('Digite o peso de 5 pessoas:')
peso = []
for p in range(1, 6):
    peso.append(float(input(f'{p}ª pessoa: '))) # .append() adiciona elementos a uma lista existente
print(f'O maior peso foi: {max(peso)}')
print(f'O menor peso foi: {min(peso)}')
'''
#forma do guanabara

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso foi de {menor}Kg')