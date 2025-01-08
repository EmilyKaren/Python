#desafio 2
a = input('\033[4;30;107mDigite algo:\033[m ')
print('\033[4;30;107m', type(a), '\033[m') # vai dizer qual o tipo de a
print('\033[4;30;107m', a.isnumeric(), '\033[m') # vai retornar true ou false se a for númerioco
print('\033[4;30;107m', a.isalpha(), '\033[m') # vai retornar true ou false se a for letra
print('\033[4;30;107m', a.isalnum(), '\033[m') # vai retornar true ou false se a for número ou letra
print('\033[4;30;107m', a.isupper(), '\033[m') # vai falar se a letra digitada esta toda com letras maiúsculas
