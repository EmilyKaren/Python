# pergunte vários nº e coloque em uma lista depois crie outras 2 listas uma com números pares e outra com números impares

lista = []
list_par = []
list_impar = []
qtde = n = 0
segrui = 'S'
while True:
    qtde = int(input('Quantos números deseja digitar: '))
    for c in range (0, qtde):
        n = (int(input(f'Digite o {c+1}º número: ')))
        lista.append(n)
        if n % 2 == 0:
            list_par.append(n)
        else:
            list_impar.append(n)
    seguir = str(input('Deseja digitar mais números [S/N]? ')).upper()
    while seguir != 'S' and seguir != 'N':
        seguir = str(input('Letra invalida! Deseja digitar mais números [S/N]? ')).upper()
    if seguir == 'N':
        break

print(f'Os números digitados foram: {lista}')
print(f'Os números PARES {list_par}\nE os ÍMPARES {list_impar}')