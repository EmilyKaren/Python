# leia um numero inteiro e diga se ele é primo ou nao
print('=-'* 5 + '\033[1;31mIdentficador de Números Primos\033[m' + '-='* 5)
m = 0
n = int(input('Digite um número: '))
for c in range(2, n):
    if n % c == 0:
        print(f'multiplo de', c)
        m += 1
if m == 0:
    print(f'O número {n} \033[4;31mÉ PRIMO!\033[m')
else:
    print(f'O número {n} \033[4;31mNÃO É PRIMO.\033[m')
print('-='* 25)

# forma do guanabara
tot = 0
num = int(input('Digite um número: '))
for i in range( 1, num+1):
    if num % i == 0:
        print('\033[33m', end= '')
        tot += 1
    else:
        print('\033[31m', end= '')
    print(i, end= ' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes!')
if tot == 2:
    print('E por isso ele é PRIMO.')
else:
    print('E por isso ele Não é primo.')