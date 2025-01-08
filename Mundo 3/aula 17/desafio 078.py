# leia 5 valores e os coloque na lista, depois mostre qual foi o maior e menor valor e suas posições

lista = []
maior = 0
menor = 0
for n in range(0,5):
    lista.append(int(input(f'Digite um número na posição {n}ª: ')))
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if menor > lista[n]:
            menor = lista[n]
print(f'Os números digitados foram: {lista}')
print(f'O MAIOR valor foi {maior} e esta na posição ', end='')
for p, v in enumerate(lista):
    if v == maior:
        print(f'{p}', end=' ')
print(f'\nO MENOR valor foi {menor} e esta na posição ', end='')
for p, v in enumerate(lista):
    if v == menor:
        print(f'{p}', end=' ')
