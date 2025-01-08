n = float(input('Digite um número: '))
par = n%2
if par == 0:
    print(f'O número {n:0.1f} é par.')
else:
    print(f'O número {n:0.1f} é ímpar.')