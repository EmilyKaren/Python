# fazer uma tabuada
from time import sleep
print('=-' *8, '\033[1mTABUADA\033[m', '-=' *8)
n = int(input('Digite um número: '))
print('Calculando...')
sleep(0.5)
for c in range(1, 11):
    print(f'{c} X {n} = ', c * n)
print('-=' *21)
