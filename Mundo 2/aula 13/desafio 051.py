# leia o primeiro termo e a razao de uma progressao aritmetica e mostre os 10 primeiros termos dessa progressao
# primeiro termo -> valor inicial
# razao -> valor utilizado para encontrar o segunto termo (primeiro termos + razao = segundo termo. primeiro termo + 2razao = terceiro termo ...)
# formula -> an = a1 + (n-1) * r
print('-=' * 20)
print('Calculando Progressão Aritmética')
a = int(input('Informe o primeiro termo:\033[1;36m '))
r = int(input('\033[mInforme a razão:\033[1;36m '))
print('Os 10 primeiros termos são:')
for p in range(1, 11):
    n = a + (p - 1) * r
    print(n, end= " -> ")
print('Acabou!')
print('\033[m-=' * 20)

#forma do guanabara

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
    print(c, end= " - ")
print('ACABOU')
