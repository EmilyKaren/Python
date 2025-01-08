# leia uma frase e diga se ela é um polindromo, ou seja, se ler ela de traz para frente significa a mesma coisa

print('\033[1m+_+ Teste de Palíndromo +_+\033[m')
print('Palíndromo, palavra ou frase que tem o mesmo significado quando escrita de traz para a frente. Vamos descobrir se você conhece uma frase com esse padrão?')
f = str((input('Digite uma frase: '))).upper() # upper tudo em maiusculo
f0 = f.split() # split separa a frase
f1 = ''.join(f0) # junta a frase
f2 = f1[::-1]
if f1 == f2:
    print(f'A palavra \033[1m{f}\033[m é um palíndromo!')
    print(f'Normal: {f1}\nInvertida: {f2}')
else:
    print(f'A palavra digitada não é um palíndromo')
    print(f'Normal: {f1}\nInvertida: {f2}')
print('\033[1m+_+ Fim do Teste +_+\033[m')

# forma do guanabara

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # solução com fatiamento
'''inverso = ''
for letra in range(len(junto) - 1, -1, -1): # solução com for
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase não é palindromo.')