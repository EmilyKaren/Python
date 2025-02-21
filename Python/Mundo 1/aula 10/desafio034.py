s = float(input('Digite o valor do seu salário: '))
if s > 1250:
    aumento = (s*10)/100
    snovo = s + aumento
else:
    aumento = (s*15)/100
    snovo = s + aumento
print(f'Você teve um aumento de R${aumento:0.2f} reais.\nSeu novo salário será de R${snovo:0.2f}')
