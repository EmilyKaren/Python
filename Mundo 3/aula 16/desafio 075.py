# digite 4 numeros e os coloque em uma tupla depois diga:
# a) quantas vezes apareceu o numero 9
# b) Em que posição apareceu o primeiro número 3
# c) quais foram os numeros pares
'''
tupla_par = ()
tupla = ()
for c in range(4):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        tupla_par += (n,)
    tupla += (n,)
cont = tupla.count(9)
pos = tupla.index(3) # quando não é digitado o número 3 da erro, já que o index não encontra ele
print(f'Os números escolhidos foram {tupla}')
print(f'O número 9 apareceu {cont} vezes')
print(f'O número 3 apareceu na {pos + 1}ª posição.')
print(f'Os números pares foram: {tupla_par}')
'''
# forma do guanabara
num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print(f'Não foi digitado o número 3.')
print('Os números pares digitados foram ',end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
