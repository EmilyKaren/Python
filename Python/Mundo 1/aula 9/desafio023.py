# na forma matematica
n = int(input('digite um número entre 0 e 9999: '))
unidade = n% 10
n = (n-unidade)/10
dezena = n % 10
n = (n-dezena)/10
centena = n % 10
n = (n-centena)/10
milhar = n
print(f'Unidade: {unidade:0.0f}\nDezena: {dezena:0.0f}\nCentena: {centena:0.0f}\nMilhar: {milhar:0.0f}')

# forma do guanabara
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')