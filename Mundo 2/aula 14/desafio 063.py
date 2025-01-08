# leia um número n e mostra os n primeiros elementos de uma sequencia fibonacci
'''
n = int(input('Digite a tamanho da sequência fibonacci: '))
ultimo = 1
penultimo = 0
count = 0
while count != n:
    termo = ultimo + penultimo
    penultimo = ultimo 
    ultimo = termo
    count += 1
    print(termo, end=' ')
print('\nFim')
'''
# forma do guanabara

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' ->',t3, end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> Fim')
print('~' * 30)
