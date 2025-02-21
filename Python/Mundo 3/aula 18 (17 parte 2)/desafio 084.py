# Leia o nome e peso de várias pessoas, depois mostre: qtde de pessoas cadastradas, uma lista com as pessoas mais pesadas, uma lista com as pessoas mais leves

continuar = 'S'
pessoas = list()
inf = list()
mai = men = 0
qtde = 0

print('='*15, 'Cadastro de pessoas', '='*15)
while True:
    if continuar == 'S':
        inf.append(str(input('Nome: ')))
        inf.append(float(input('Peso: ')))
        if len(pessoas) == 0:
            mai = men = inf[1]
        else:
            if inf[1] > mai:
                mai = inf[1]
            if inf[1] < men:
                men = inf[1]
        pessoas.append(inf[:])
        qtde += 1
        inf.clear()
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    elif continuar != 'N':
        continuar = str(input('Letra invalida! Deseja continuar? [S/N] ')).upper()
    else:
        break
print('='*50)
# existem 2 formas de contar a quantidade de pessoas que foram cadastradas. A primeira com um contador e a segunda usando o len(pessoas)
print(f'Ao todo, você cadastrou {qtde} pessoas.')
print(f'Pessoas com o peso maior ou igual a {mai} Kg: ', end='')
for p in pessoas:
    if p[1] == mai:
        print(p[0], end=' ')
print()
print(f'Pessoas com o peso menor ou igual a {men} Kg: ', end='')
for p in pessoas:
    if p[1] == men:
        print(p[0], end='')
