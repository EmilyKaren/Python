#jogo de pedra papel e tesoura
from random import choice
print('\033[90m-=\033[m'*20)
print('🎮 Vamos jogar pedra papel e tesoura!🕹️')
j1 = (str(input('Digite sua escolha ✂️  🏔️  📃: ')).upper()).strip()
if j1 == 'PEDRA' or j1 == 'PAPEL' or j1 == 'TESOURA':
    lista = ['PEDRA', 'PAPEL', 'TESOURA']
    j2 = choice(lista)
    print(f'\033[1;90;44m  * ✂️  🏔️  📃 * PLACAR: * ✂️  🏔️  📃 *  \033[m\n* j1 \033[1m{j1}\033[m X j2 \033[1m{j2} \033[m*')
    if j1 == 'PEDRA' and j1 != j2:
        if j2 == 'PAPEL':
            print('Você \033[4;31mperdeu\033[m. O computador \033[4;32mvenceu!\033[m')
        else:
            print(f'j1 \033[1m{j1}\033[m X j2 \033[1m{j2}\033[m')
            print('\033[1;32mVocê venceu!\033[m')
    elif j1 == 'PAPEL'  and j1 != j2:
        if j2 == 'TESOURA':
            print('Você \033[4;31mperdeu\033[m. O computador \033[4;32mvenceu!\033[m')
        else:
            print('\033[1;32mVocê venceu!\033[m')
    elif j1 == 'TESOURA' and j1 != j2:
        if j2 == 'PEDRA':
            print('Você \033[4;31mperdeu\033[m. O computador \033[4;32mvenceu!\033[m')
        else:
            print('\033[1;32mVocê venceu!\033[m')
    else:
        print(f'\033[4;33mEMPATE!\033[m')
else:
  print(f'\033[4mO que você digitou \033[33m{j1}\033[m \033[4mnão corresponde com pedra, paple ou tesoura.\nTente novamente!\033[m')
print('\033[90m-=\033[m'*20)
