# leia o nome e preço de varios produtos e seus nomes, depois pergunte se o usuário vai continuar. No final mostre o total gasto, quantos produtos custam mais de 1000 e qual o mais barato

maior = soma = cont = 0
nome_menor = ''
print('--' *30)
print('LOJA TUDO UM POUCO'.center(50))
print('--' *30)
while True:
    continuar = ''
    nome = str(input('Informe o nome do produto: '))
    preço = float(input('Informe o preço do produto: '))
    soma += preço
    cont += 1
    if preço > 1000:
        maior += 1
    if cont == 1 or preço < menor:
        menor = preço
        nome_menor = nome
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja cadastrar mais produtos? [S/N] ')).upper()
    if continuar == 'N':
        break
print('=-' *30)
print(f'O total gasto foi de R$ {soma:0.2f}')
print(f'Foram {maior} produtos com mais de R$ 1000,00 reias.')
print(f'O produto mais barato foi {nome_menor}, custando R$ {menor:0.2f}')