# crie uma tupla com varias palavras (sem assento) e mostre quais vogais cada palavra tem.

'''
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for frase in palavras:
    vogais = ''
    a = frase.count('a')
    e = frase.count('e')
    i = frase.count('i')
    o = frase.count('o')
    u = frase.count('u')
    if a >= 1:
        for q in range(a):
            vogais += 'a '
    if e >= 1:
        for q in range(e):
            vogais += 'e '
    if i >= 1:
        for q in range(i):
            vogais += 'i '
    if o >= 1:
        for q in range(o):
            vogais += 'o '
    if u >= 1:
        for q in range(u):
            vogais += 'u '
    print(f'Na palavra \033[1;36m{frase.upper()}\033[m temos as vogais \033[1;36m{vogais.upper()}\033[m')
'''

# forma do guanabara
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra \033[1;36m{p.upper()}\033[m temos as vogais ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print('\033[1;36m'+letra+'\033[m', end=' ')