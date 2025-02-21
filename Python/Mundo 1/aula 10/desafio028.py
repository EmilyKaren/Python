from random import randint
from time import sleep # faz o computador esperar uma certa quantidade de tempo antes de processeguir com o código
print('\033[33m¨*¨\033[m' * 20)
print('Tente descobrir o número que eu escolhi!')
print('\033[1;37m-=-\033[m' * 20)
n = int(input('Digite um número entre 0 e 5: '))
print('\033[1;34;40mProcessando...\033[m')
sleep(2) # espera 2 segundos antes de continuar 
na = randint(0, 5)
if n == na:
    print(f'\033[4;32mParabens\033[m você acertou! O número era \033[4;32m{na}\033[m.')
    print('\033[33m¨*¨\033[m' * 20)
else:
    print(f'\033[1;31mNão foi desta vez!\033[m Eu pensei no número \033[4;32m{na}\033[m e não no \033[4;31m{n}\033[')