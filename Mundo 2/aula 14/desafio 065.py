# leia varios números e no final mostre a media entre eles e qual foi o maior e menor número, por fim pergunte ao usuário se ele quer continuar a digitar
print('===== Calculadora de Médias =====')
n = 0
soma = 0
maior = 0
menor = 10
cont = 0
r = 'S'
while r == 'S':
    n = float(input('Digite um número: '))
    r = str(input('Quer continuar [S/N]: ')).upper()
    cont += 1
    soma += n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
media = soma / cont
print(f'A média entre os número é {media}')
print(f'O maior número é {maior}')
print(f'E o menor número é {menor}')
