print('Vamos descobrir qual o maior e menor número!')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print(f'O número {n1} é o maior.')
    if n2 > n3:
        print(f'E o número {n3} é o menor')
    else:
        print(f'E o número {n2} é o menor.')
if n2 > n1 and n2> n3:
    print(f'O número {n2} é o maior.')
    if n1 > n3:
        print(f'E o número {n3} é o menor.')
    else:
        print(f'E o número {n1} é o menor.')
if n3 > n1 and n3 > n2:
    print(f'O número {n3} é o maior.')
    if n1 > n2:
        print(f'E o número {n2} é o menor.')
    else:
        print(f'E o número {n1} é o menor.')

#forma do guanabara

print('Vamos descobrir qual o maior e menor número!')
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# verificando que é o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# verificando que é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O menor número é {menor}.\nO maior número é {maior}.')
