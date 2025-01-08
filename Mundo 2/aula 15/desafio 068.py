# jogue par ou impar, o jogo só acaba quando o o jogador perder e no final tem que mostrar o total de vitorias consecutivas

import random

soma = cont = 0
continuar = 'S'

while continuar == 'S':
    while True:
        escolha = str(input('Qual sua Escolha par ou impar? ')).upper()
        n_jogador = int(input('Agora escolha um número [0, 10]: '))
        n_computador = random.randrange(0, 10)
        soma = n_computador + n_jogador
        print(f'A soma dos números {n_jogador} mais {n_computador} deu {soma} ')
        if escolha == 'PAR':
            if soma % 2 == 0:
                print(f'Resultado -> PAR\nPonto para o jogador!')
                cont += 1
            else:
                print(f'Resultado -> IMPAR\nO jogador perdeu!')
                break
        elif escolha == 'IMPAR':
            if soma % 2 != 0:
                print(f'Resultado -> IMPAR\nPonto para o jogador!')
                cont += 1
            else:
                print(f'Resultado -> PAR\nO jogador perdeu!')
                break
    print(f'O jogador venceu {cont} rodada(s) seguidas!')
    continuar = str(input('Deseja continuar o jogo?[S/N] ')).upper()
print('Fim de jogo!')
