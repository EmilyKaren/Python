# digite uma expressao que tenha parenteses e analise se os parenteses foram colocados de maneira correta
'''
e = str(input('Digite uma expressão: '))
qtde = e.count('(')
q = e.count(')')
#print(e, qtde, q)
if qtde == q:
    print(f'Expressão valida!')
else:
    print(f'Expressão invalida!')
'''
# forma do guanabara
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão é inválida T_T')