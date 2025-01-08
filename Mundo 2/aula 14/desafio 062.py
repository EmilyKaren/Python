# melhore o desafio 61, quando o programa terminar de mostrar os 10 termos pergunte ao usuário se ele quer ver mais quantos termos ou se ele quer parar.

n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite o valor da razão: '))
cont = 0
adicionar = -1
qtd = 11
while adicionar != 0:
    qtd += adicionar
    while cont != qtd:
        cont += 1
        pa = n1 + r * (cont - 1)
        print(f'{cont}º termo = {pa}')
    print('Caso queira que o programa pare digite 0')
    adicionar = int(input('Quantos termos a mais deseja ver: '))
print(f'Estes foram os {cont} primeiros termos!')
