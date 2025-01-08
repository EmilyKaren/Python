# escreva uma tupla de 0 à 20 por extenso, e peça ao usuário para digitar um número e mostre-o

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dizesseis', 'dezessete', 'dezoito' , 'dezenove', 'vinte')

cont = 0
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n > 20 or n < 0:
        n = int(input('Número inválido! Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numero[n]}')
    cont += 1
    repetir = str(input('Você quer continuar? [S/N] ')).upper()
    if repetir == 'N':
        break
print(f'Você viu {cont} números por extenso!')
