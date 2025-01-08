#interrompendo repetições while
'''
enquanto Verdadeiro             while True:
    se caminho                      if caminho:
        passo                           passo
    se buraco                       if buraco:
        pula                            pula
    se moeda                        if moeda:
        pega                            pega
    se trofeu                       if trofeu:
        pula                            pula
        interrompa                      break
pega                             pega
'''

# para o while entrar em um loop infinito basta colocar TRUE na frente, e para ele parar basta colocar o BREAK no final

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma de todos os número é {s}')
