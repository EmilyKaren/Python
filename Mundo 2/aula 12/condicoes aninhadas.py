''' Condicao aninhada é uma condicao dentro da outra

se carro.esquerda()                 if carro.esquerda():
    vire esquerda                       vire esquerda
senão se carro.direita()            elif carro.direita():
    vire direita                        vire direita
senão                               else:
    sigua em frente                     sigua em frente

Pode ser colocado quantos elif forem necessários entre um if e um else.
Caso queira pode tirar o último else
'''
# prática
nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('É o mesmo nome do professor do curso em video!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Ana':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem comum.')
print(f'Seja bem vindo(a), {nome}!')
