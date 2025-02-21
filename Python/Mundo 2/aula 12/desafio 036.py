# aprovar emprestimo
from time import sleep
valor = float(input('Digite qual o valor da casa que deseja comprar: '))
tempo = float(input('Em quantos anos pretende pagar a casa: '))
sal = float(input('Por fim, informe quanto é o seu salário: '))
meses = tempo * 12
vmensal = valor/meses
exceder = (sal*30)/100
print('=*=' * 20)
print(f'Para aprovarmos o emprestimo as parcelas não podem \033[4;33mexceder\033[m 30% do seu salário!')
print('\033[1;34mCalculando...\033[m\n')
sleep (2)
if vmensal > exceder:
    print(f'\033[4;31mEmpréstimo Negado\033[m')
else:
    print(f'\033[4;32mEmpréstimo Aprovado\033[m')
print(f'Valor da parcela mensal é de R$ {vmensal:0.2f}')
print(f'30% do seu salário equivale a R$ {exceder:0.2f}')
