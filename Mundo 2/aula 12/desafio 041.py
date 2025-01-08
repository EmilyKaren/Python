# mostrar a categoria do atleta de acordo com sua idade
from datetime import date
print('\nCategorias:')
print('\033[1;34mMirim:\033[m Até 9 anos.\n\033[1;34mInfantil:\033[m Até 14 anos.\n\033[1;34mJunior:\033[m Até 19 anos.\n\033[1;34mSênior:\033[m Até 20 anos.\n\033[1;34mMaster:\033[m Acima de 20 anos.\n')
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'Sua categoria é \033[1;34mMirim\033[m. E sua idade é {idade} anos.')
elif idade <= 14:
    print(f'Sua categoria é \033[1;34mInfantil\033[m. E sua idade é {idade} anos.')
elif idade <= 19:
    print(f'Sua categoria é \033[1;34mJunior\033[m. E sua idade é {idade} anos.')
elif idade == 20:
    print(f'Sua categoria é \033[1;34mSênior\033[m. E sua idade é {idade} anos.')
else:
    print(f'Sua categoria é \033[1;34mMaster\033[m. E sua idade é {idade} anos.')
