# fazer tipo uma calculadora

print('Calculadora')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
menu = 0
while menu != 5:
    print('==-=='* 10)
    print('Qual opção você deseja realizar?')
    menu = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\nSua escolha: '))
    if menu == 1:
        print(n1 + n2)
        print('==-=='* 10)
    elif menu == 2:
        print(f'{n1} X {n2} = ', n1 * n2)
        print('==-=='* 10)
    elif menu == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
            print('==-=='* 10)
        elif n1 == n2:
            print('Os dois números possuem o mesmo valor!')
            print('==-=='* 10)
        else:
            print(f'O maior número é {n2}')
            print('==-=='* 10)
    elif menu == 4:
        n1 = float(input('Insira os novos números.\nDigite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print('==-=='* 10)
    elif menu == 5:
        print('Fim do programa!')
print('==-=='* 10)