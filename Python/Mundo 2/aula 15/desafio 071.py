# simule um caixa eletronico, pergunte quanto o usuário ira sacar depois fale quantas celulas de cada valor serão entregues [50, 20, 10, 1]
'''
n = notas50 = notas20 = notas10 = notas1 = sacar = 0

valor = int(input('Qual valor você vai sacar: '))
while True:
    if valor >= 50:
        notas50 = valor // 50
        valor = valor % 50
    if valor >= 20:
        notas20 = valor // 20
        valor = valor % 20
    if valor >= 10:
        notas10 = valor // 10
        valor = valor % 10
    if valor >= 1:
        notas1 = valor // 1
        valor = valor % 1
    break
sacar = notas50 * 50 + notas20 * 20 + notas10 * 10 + notas1
print(f'Você vai sacar:')
print(f'{notas50} notas de R$50')
print(f'{notas20} notas de R$20')
print(f'{notas10} notas de R$10')
print(f'{notas1} notas de R$1')
'''

# forma guanabara
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
