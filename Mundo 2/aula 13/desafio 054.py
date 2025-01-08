# leia a data de aniversário de 7 pessoas e diga quantas atingiram a maior idade e quantas ainda não
from datetime import date
maior = 0
menor = 0
ano = date.today().year
print('A entrada é permitida para no máximo 7 pessoas e precisamos saber quantas são maiores de idade, informe no campo abaixo o ano de nascimento dos participantes.\nCaso seja menos de 7 participantes digite 0 no lugar do ano')
for p in range(0, 7):
    a1 = int(input('Ano: '))
    if ano - a1 >= 21 and a1 != 0:
        maior += 1
    else:
        if a1 != 0:
            menor += 1
print(f'Total de pessoas maiores de idade: {maior}')
print(f'Total de pessoas menores de idade: {menor}')
