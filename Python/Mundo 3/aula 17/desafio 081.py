# leia varios valores (pergunte se deseja continuar), depois mostre quantos numeros foram digitados a lista decrescente e se o numero 5 foi digitado 

lista = []
seguir = 'S'
cont = 0
while True:
    for c in range(0, 5):
        lista.append(int(input('Digite um número: ')))
        cont += 1
    seguir = str(input('Deseja continuar [S/N]: ')).upper()
    if seguir != 'S' and seguir != 'N':
        while seguir != 'S' and seguir != 'N':
            seguir = str(input('Digite uma letra válida! Deseja proseguir[S/N]? ')).upper()
        if seguir == 'N':
            break
    elif seguir == 'N':
        break

print(f'Foram digitados {cont} números.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente:\n{lista}')
if 5 in lista:
    print(f'O número 5 apareceu {lista.count(5)} vez(es) e na apareceu pela primeira vez na posição {lista.index(5)}')
else:
    print('Não foi digitado o número 5.')
