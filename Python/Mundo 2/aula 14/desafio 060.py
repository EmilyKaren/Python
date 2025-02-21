# ler um número qualquer e mostrar seu fatorial, a forma de mostrar um fatorial é Número + exclamação

print('Calculando o fatorial com while!')
n = int(input('Digite o número: '))
cont = 0
mult = n
print(n, end='')
while cont != n - 1:
    cont += 1
    mult *= cont
    print(f' X {cont}', end='')
print(' =', mult)
print(f'O fatorial de {n} é {mult}')

# versão com for

print('\nCalculando o fatorial com for!')
n1 = int(input('Digite um número: '))
mult = n1
print(n, end='')
for cont in range(1, n1):
    mult *= cont
    print(f' X {cont}', end='')
print(' =', mult)
print(f'O fatorial de {n1} é {mult}')

# fazer o número aparecer de traz para frente (forma guanabara)

n = int(input('Digite um número: '))
c = n
f = 1
while c > 0:
    print(c, end=' ')
    print('X ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f)
