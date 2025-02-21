# Listas Compostas - listas dentro de listas
'''
se for adicionar uma lista dentro de outra lista lembre-se de colocar [:], caso não coloque você irá apenas repetir conteúdo e não inserir um novo
quando usa dado[:] você esta fazendo uma cópia | quando usa dado[] você esta usando o dado original e se o for colocar dentro de outra lista você estará fazendo uma ligação
'''
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print('-'*30)
#-----------------------

pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoas[0]) # pega todos os dados da lista na posição 0
print(pessoas[2][1]) # pega a lista na posição 2 o item que esta na posição 1
print(pessoas[2:]) # pega as listas da 2ª posição ate o final
print('-'*30)
#-----------------------

pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in pessoas: # para cada pessoa em pessoa
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('-'*30)
#------------------------

galera = list()
dado = list()
for c in range(0, 3): # le os dados e os coloca dentro de galera, e no final apaga os dados de dado
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

total_maior = total_menor = 0
for p in galera: # para saber se a pessoa é maior ou menor de idade
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1
print(f'Temos {total_maior} maiores e {total_menor} menores de idade.')
print('-'*30)
#------------------------
