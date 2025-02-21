# o usuário ira digitar varios numeros (qtd indefinida) e caso seja digitado um numero repetido ele não entra na lista. no final mostre todos os números digitados em ordem crescente
'''
lista = []
vl_unico = []
cont = 5
while True:
    for n in range(0, cont):
        lista.append(int(input('Digite um número: ')))
    p = str(input('Deseja inserir mais números? [S/N] ')).upper()
    if p == 'N':
        break
    elif p == 'S':
        cont = int(input('Quantos valores deseja adicionar: '))
for n in lista:
    if n not in vl_unico:
        vl_unico.append(n)
vl_unico.sort()
print(f'Os números digitados foram: {vl_unico}')
'''
lista = []
p = 'S'
while p == 'S':
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor já inserido na lista!')
    p = str(input('Deseja continuar [S/N]?')).upper()
lista.sort()
print(f'Os valores digitados foram {lista}')