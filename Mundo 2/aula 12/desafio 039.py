# informar se a pessoa tem ou não que se alistar/apresentar no exercito
from datetime import date
ano = int(input('Informe em que ano você nasceu: '))
genero = str(input('Informe seu gênero: ').upper()).strip()
idade = date.today().year - ano
print(f'\033[1mVocê tem {idade} anos.\033[m')
if genero == 'MASCULINO':
    print('\033[4mSeu alistamento é obrigatório.\033[m')
    if idade == 18:
        print(f'\033[1;32mEsta na hora de se alistar/apresentar no exercito. Boa sorte!\033[m')
    elif idade > 18:
        print(f'\033[1;31mVocê está {idade-18} anos atrasado para se alistar/apresentar no exercito, não perca tempo!\nSeu alistamento era no ano {date.today().year - (idade - 18)}.\033[m')
    else:
        print(f'\033[1;33mAinda falta {18-idade} anos para você se alistar/apresentar no exercito.\nSeu alistamento será no ano {date.today().year + (18 - idade)}. Aproveite esse tempo!\033[m')
elif genero == 'FEMININO':
    print('\033[4mSeu alistamento não é obrigatório.\033[m')
    cadastro = int(input('Deseja ver em que ano você pode se alistar?\n[1] Sim\n[2] Não\nSua opção: '))
    if cadastro ==  1:
        if idade == 18:
            print(f'\033[1;32mEsta na hora de se alistar/apresentar no exercito. Boa sorte!\033[m')
        elif idade > 18:
            print(f'\033[1;31mVocê está {idade-18} anos atrasado para se alistar/apresentar no exercito, não perca tempo!\nSeu alistamento era no ano {date.today().year - (idade - 18)}.\033[m')
        else:
            print(f'\033[1;33mAinda falta {18-idade} anos para você se alistar/apresentar no exercito.\nSeu alistamento será no ano {date.today().year + (18 - idade)}. Aproveite esse tempo!\033[m')
    else:
        print('Tenha um bom dia!')
else:
    print('A informação digitada não corresponde com as opções dadas.\nTente novamente!')
