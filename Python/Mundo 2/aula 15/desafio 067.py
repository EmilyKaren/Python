# mostre a tabuada para cada número digitado pelo usuário, o programa só para quando o número for negativo
print('=-' * 10, 'TABUADA', '=-' * 10)
print('Para parar digite um número negativo!')
while True:
    n = int(input('Digite um número: '))
    if n >= 0:
        print(f'A tabuada do número {n} é:')
        for c in range (1, 11):
            print(f'{c} X {n} = {c * n}')
        print('=-' * 20)
    else:
        print('Fim do Programa!')
        print('=-' * 20)
        break