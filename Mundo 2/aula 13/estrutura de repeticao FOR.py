# Laço de repetição / Iteração / Estrutura de repetição
'''
laço c no intervalo(1,10)        for c in range(1,10):
    passo                           passo
pega                             pega 

laço c no intervalo(0,3)         for c in range(0,3):
    passo                           passo
    pula                            pula
passo                            paso
pega                             pega

laço c no intervalo(0,3)        for c in rage(0,3):
    se tiver moeda                  if tiver moeda:
        pega                            pega
    passo                           passo
    pula                            pula
passo                           passo
pega                            pega
'''
for c in range(0,6):
    print('Oi')
print('Fim')

for c in range(1,6): # o ultimo ele "ignora"
    print(c)
print('Fim')

for i in range(6, 0, -1): # conta para traz
    print(i)
print('Fim')

for i in range(0, 7, 2): # conta de zero ate sete pulando de dois em dois
    print(i)
print('Fim')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim da contagem!')

i = int(input('Início: ')) # em qual nº de bloco começa
f = int(input('Fim: ')) # em qual bloco termina
p = int(input('Passos: ')) # quantos passos vai dar, e vai mostrar em qual bloco você "pararia"
for c in range(i, f+1, p):
    print(c)
print('Fim da caminhada!')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n # -> s = s + n
print(f'A soma de todos os valores é {s}')