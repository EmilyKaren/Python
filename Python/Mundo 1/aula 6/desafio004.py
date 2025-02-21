a = input('\033[30;42mDigite qualquer coisa pelo teclado:\033[m ')
# a função input retorna sempre o tipo string
print(f'O item que você digitou é do tipo \033[4;32m{type(a)}\033[m, e suas outras informações são:')
print(f'É númerico? \033[4;31m{a.isnumeric()}\033[m')
print(f'É alfabeto? \033[4;30m{a.isalpha()}\033[m')
print(f'É alfanumerico? \033[4;97m{a.isalnum()}\033[m')
print(f'Todas as suas letras são maiúsculas? \033[4;33m{a.isupper()}\033[m')
print(f'Todas as suas letras são minúsculas? \033[4;34m{(a.islower())}\033[m')
print(f'Esta capitalizada? \033[4;35m{a.istitle()}\033[m') # capitalizada seria a primeira letra maiúscula e o resto minúsculo
print(f'O que você digitou é \033[1;36m{a}\033[m')
