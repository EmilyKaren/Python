# leia o nome e a média do aluno e coloque em um dicionário, crie também a situação e coloque caso a média seja maior que 7 aprovado, caso contrário reprovado

inf = dict()

inf['nome'] = str(input("Digite o nome: "))
inf['média'] = float(input(f"Digite a média de {inf['nome']}: "))
if inf['média'] >= 7:
    inf['situação'] = "Aprovado"
elif inf['média'] < 7 and inf['média'] >= 5:
    inf['situação'] = 'Recuperação'
else:
    inf['situação'] = "Reprovado"
print('-=' * 30)
for k, v in inf.items():
    print(f'{k} é igual a {v}.')
