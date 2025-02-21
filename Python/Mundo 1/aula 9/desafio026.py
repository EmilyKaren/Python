f = input('Digite uma frase: ')
print(f'Quantas vezes aparece a letra A: {f.count('a')}') # conta quantas vezes aparece a letra a
print(f'A letra A aparece pela primeira vez no caractere {f.find('a')}') # informa em qual casa aparece pela primeira vez
print(f'E aparece pela última vez no caractere {f.rfind('a')}') # informa em qual casa aparece pela última vez

# forma do Guanabara
f = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {f.count('A')} vezes')
print(f'A letra A aparece pela primeira vez no caractere {f.find('A')+1}')
print(f'E aparece pela última vez no caractere {f.rfind('A')+1}')
