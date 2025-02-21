# refazer o exercicio 51, fazer uma PA
# leia o primeiro termo e a razao de uma progressao aritmetica e mostre os 10 primeiros termos dessa progressao
# primeiro termo -> valor inicial
# razao -> valor utilizado para encontrar o segunto termo (primeiro termos + razao = segundo termo. primeiro termo + 2razao = terceiro termo ...)
# formula -> an = a1 + (n-1) * r
'''termo = primeiro termo[n1] + razão. E termo = primeiro termo[n1] '''

n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite o valor da razão: '))
cont = 0
while cont != 10:
    cont += 1
    pa = n1 + r * (cont - 1)
    print(f'{cont}º termo = {pa}')
print('Estes foram os 10 primeiros termos!')
