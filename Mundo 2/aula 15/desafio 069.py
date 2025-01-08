# leai a idade e o sexo de varias pessoas e pergunte se o usuário que continuar ou não e no final mostre quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos.

cont_F = cont_M = cont_I = 0

print('======== CADASTRO ========')
while True:
    s = ''
    continuar = ''
    i = int(input('Digite a idade da pessoa: '))
    while s != 'F' and s != 'M':
        s = str(input('Digite o sexo da pessoa [M/F]: ')).upper()
    if s == 'F':
        if i < 20:
            cont_F += 1
            if i > 18:
                cont_I += 1
        elif i > 18:
            cont_I += 1
    elif s == 'M':
        cont_M += 1
        if i > 18:
            cont_I += 1
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print('=' * 26)
print(f'Foram cadastrados no total:')
print(f'{cont_I} pessoas com mais de 18 anos.')
print(f'{cont_M} homens.')
print(f'{cont_F} mulheres com menos de 20 anos.')
