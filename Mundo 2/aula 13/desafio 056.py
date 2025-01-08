# leia o nome, idade e sexo de 4 pessoas e diga: a media da idade do grupo, o nome do homem mais velho e quantas mulheres tem menos de 20 anos
'''
m = 0
q = 0
idade = []
nome = []
sexo = []
print('\033[1mDigite o nome, idade e sexo dos participantes:\033[m')
for c in range(0, 4):
    nome.append(str(input('Nome: ')))
    idade.append(int(input('Idade: ')))
    sexo.append(str(input('Sexo: ')).upper())
    q += 1
for i in range(0, 4):
    if sexo[0] == 'FEMININO' and idade[0] < 20:
        m +=1
    elif sexo[1] == 'FEMININO' and idade[1] < 20:
        m +=1
    elif sexo[2] == 'FEMININO' and idade[2] < 20:
        m +=1
    elif sexo[3] == 'FEMININO' and idade[3] < 20:
        m += 1
if sexo[0] == 'MASCULINO':
    if idade[0] > idade[1] or idade[0] > idade[2] or idade[0] > idade[3]:
        print(f'O homem com maior idade é \033[1;36m{nome[0]}\033[m')
elif sexo[1] == 'MASCULINO':
    if idade[1] > idade[2] or idade[1] > idade[3]:
        print(f'O homem com maior idade é \033[1;36m{nome[1]}\033[m')
elif sexo[2] == 'MASCULINO':
    if idade[2] > idade[3]:
        print(f'O homem com maior idade é \033[1;36m{nome[2]}\033[m')
elif sexo[3] == 'MASCULINO':
        print(f'O homem com maior idade é \033[1;36m{nome[3]}\033[m')
print(f'A média das idades é \033[1;32m{sum(idade)/q:0.2f}\033[m')
print(f'A quantidade de mulheres com menos de 20 anos é \033[1;33m{m}\033[m')
'''
# forma do guanabara
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20 = 0
for p in range(1, 5):
    print(f'---- {p}ª PESSOA ----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulher20 += 1

mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {mulher20} mulheres com menos de vinte anos.')