# gere 5 números aleatorios e os coloque em uma tupla depois mostre a listagem de números e diga qual o menor e o maior número

from random import randint

tupla = ()
for c in range(0,5):
    n = random.randint(0, 10)
    tupla += (n,)

maior = tupla[0]
menor = tupla[0]
for num in tupla:
    if maior < num:
        maior = num
    elif menor > num:
        menor = num

print(f'Os números sorteados foram {tupla}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')

# forma do guanabara
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi {max(numeros)}')
print(f'O menor número sortedo foi {min(numeros)}')
