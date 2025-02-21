# Laços de repetição Parte 2
'''
enquanto não maçã       while not maçã:
    passo                   passo
pega                    pega
------------------------------------------------------------------
enquanto não maçã       while not maçã:
    se chão                 if chão:
        passo                   passo
    se buraco               if buraco:
        pula                    pula
    se moeda                if moeda:
        pega                    pega
pega                    pega
------------------------------------------------------------------
versão em for:                  versão em while:
    for c in range(1, 10):      c = 1
        print(c)                while c < 10:
    print('Fim')                    print(c)
                                    c += 1
                                print('Fim')
------------------------------------------------------------------
Em ambos o resultado é o mesmo!
Sei o limite -> for, while
Não sei o limite -> while
'''

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('Fim')

c = 1
par = impar = 0
while c != 0:
    c = int(input('Digite um valor: '))
    if c != 0:
        if c % 2 == 0:
            par +=1
        else:
            impar += 1
print(f'A quantidade de números pares foi {par} e de números ímpares foi de {impar}.')
