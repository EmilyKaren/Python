# jogo do adivinhe o número, mostrando quantas tentativas foram necessarias para vencer
from random import randint
from time import sleep

computador = randint(0, 10)
tentativas = 0
jogada = ''
print('\033[1;34m=+='* 7, 'JOGO DE ADVINHAÇÃO', '=+='* 7, '\033[m')
print('Tente adivinhar entre 0 e 10 o número que estou pensando!\nPreparado?')
sleep(1)
print('\033[1;31mPEN...\033[m')
sleep(1)
print('\033[1;33mSAN...\033[m')
sleep(1)
print('\033[1;32mDO!\033[m')
sleep(1)
print(computador)
while computador != jogada:
    jogada = int(input('\033[1mFaça sua jogada!\033[m\n'))
    tentativas += 1
    if computador != jogada:
        print('\033[4;31mERROU!\033[m Tenta de novo.')
print(f'Parabens você acertou! Eu pensei no número \033[4;32m{computador}\033[m.')
if tentativas > 1 and tentativas <= 4:
    print('Tenho que admitir, você foi muito bem!')
elif tentativas == 1:
    print(f'Uau!! Você acertou de primeira, que sorte!!')
elif tentativas >= 5 and tentativas <= 7:
    print('Você conseguiu, mas precisou de muitas tentativas dúvido acertar com menos!')
elif tentativas >= 8 and tentativas < 10:
    print('Chutou quase todos os números em, mas pelo menos acertou.')
else:
    print('Só acertou porque não tinha mais números para chutar!')
print(f'Precisou de \033[4;32m{tentativas}\033[m tentativas.')
print('\033[1;34m=+=\033[m'* 20)
