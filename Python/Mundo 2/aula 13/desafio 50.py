# mostrar os numeros de 1 a 6 e a soma dos numeros pares
s = 0
for c in range(1, 7):
    print(c)
    if c % 2 == 0:
        s += c
print(f'A soma dos números pares é {s}')

# leia seis numeros inteiros e mostre a soma dos numeros pares
m = 0
for i in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        m += num
print(f'A soma dos números pares é {m}')
