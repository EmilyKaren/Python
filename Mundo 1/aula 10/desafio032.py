ano = int(input('Digite um ano: '))
bi = ano%4
if bi == 0:
    print(f'O ano {ano} é BISSEXTO. Logo, o mês de fevereiro terá 29 dias.')
else:
    print(f'O ano {ano} não é bissexto.')

'''forma do guanabara
Ano bissexto é todo número divisivel por 4, exceto anos multiplos de 100 que não são multiplos de 400.'''

from datetime import date
ano = int(input('Qual ano quer analisar? Caso queira analisar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO É BISSEXTO!')
