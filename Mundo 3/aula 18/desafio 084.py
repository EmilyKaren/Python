# Leia o nome e peso de várias pessoas, depois mostre: qtde de pessoas cadastradas, uma lista com as pessoas mais pesadas, uma lista com as pessoas mais leves

continuar = 'S'
pessoas = list()
inf = list()
maior = list()
menor = list()
qtde = 0

print('='*15, 'Cadastro de pessoas', '='*15)
while True:
    if continuar == 'S':
        inf.append(str(input('Nome: ')))
        inf.append(int(input('Peso: ')))
        pessoas.append(inf[:])
        qtde += 1
        inf.clear()
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    elif continuar != 'N':
        continuar = str(input('Letra invalida! Deseja continuar? [S/N] ')).upper()
    else:
        break
for p in pessoas:
    if p[1] >= 100:
        maior.append(p[0])
    elif p[1] <= 70:
        menor.append(p[0])
print('='*50)
print(f'Ao todo, você cadastrou {qtde} pessoas.')
print(f'Pessoas com o peso maior ou igual a 100 Kg: {maior}.')
print(f'Pessoas com o peso menor ou igual a 70 Kg: {menor}.')
