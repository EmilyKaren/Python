# codificar em binário, hexadecimal e octal
n = int(input('Digite um número \033[4;34minteiro\033[m que você deseja decodificar: '))
forma = int(input('Caso queira codificar para \033[4;36mbinário\033[m digite \033[4;36m[1]\033[m.\nCaso seja \033[4;35mhexadecimal\033[m digite \033[4;35m[2]\033[m.\nCaso seja em \033[4;34moctal\033[m digite \033[4;34m[3]\033[m.\nCaso seja as \033[4;33mtrês opções\033[m digite \033[4;33m[4]\033[m.\n'))
if forma == 1:
    print(f'O número \033[4;34m{n}\033[m códificado em binário fica:')
    print('\033[4;36m',bin(n)[2:],'\033[m')
elif forma == 2:
    print(f'O número \033[4;34m{n}\033[m códificado em hexadecimal fica:')
    print('\033[4;35m',hex(n)[2:],'\033[m')
elif forma == 3:
    print(f'O número \033[4;34m{n}\033[m códificado em octal fica:')
    print('\033[4;34m',oct(n)[2:],'\033[m')
elif forma == 4:
    print(f'O número \033[4;34m{n}\033[m códificado nas três opções fica:')
    print('\033[4;36mBinário:',bin(n)[2:],'\033[m')
    print('\033[4;35mHexadecimal:',hex(n)[2:],'\033[m')
    print('\033[4;34mOcatal:',oct(n)[2:],'\033[m')
else:
  print(f'A opção digitada \033[4;34m{forma}\033[m  não corresponde com as opções dadas.\nTente novamente!')
print('Volte sempre!')
