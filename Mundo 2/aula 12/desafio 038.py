# Mostrar o maior número 
print('\033[1;33m--*--\033[m' * 20)
print('Vou te dizer qual número inteiro é o maior, então me diga')
n1 = int(input('Qual o primeiro número: '))
n2 = int(input('Qual o segundo número: '))
if n1 > n2:
    print(f'O MAIOR número é {n1}, e o menor número é {n2}.')
    print(f'Logo o PRIMEIRO número é maior!')
elif n2 > n1:
    print(f'O MAIOR número é {n2}, e o menor número é {n1}.')
    print(f'Logo o SEGUNDO número é maior!')
else:
    print('Os dois números tem o mesmo valor!')
print('\033[1;33m--*--\033[m' * 20)
