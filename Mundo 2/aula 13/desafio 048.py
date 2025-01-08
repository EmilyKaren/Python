# mostrar a soma de todos os numeros impares multiplos de 3 no intervalo de 1 ate 500
t = 0
s = 0
print('Números ímpares multiplos de 3 de 1 até 500:')
for n in range(0, 501):
    if n % 2 != 0:
        if n % 3 == 0:
            print(n)
            s += n
            t += 1
print(f'A soma de todos os \033[4m{t}\033[m números é \033[4m{s}\033[m')

# forma do guanabara
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma de todos os {cont} valores solicitados é {soma}')
