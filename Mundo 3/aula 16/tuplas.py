# Variáveis Compostas - Tuplas
'''
    AS TUPLAS SÃO IMUTÁVEIS!
A única forma de "mudar" uma tupla é apagando ela da memória usando o del
Tem como criar uma tupla sem os parenteses
quando utiliza números negativos dentro dos colchetes [] a contagem/seleção acontece de trás para frente.
Tem como juntar duas tuplas utilizando o +, e nesses casos a ordem pode influenciar o resultado.
Quando faz o fatiamento[1:5] o espaço "5" é ignorado, logo neste exemplo vai ir do 1 ao 4. E quando deixa os : sozinhos vai até o final ex: 
    [4:] -> do 4 até o final
    [:3] -> do início ate o 3
len() -> conta quantas palavras/frases tem dentro da tupla
enumerate() -> funciona como um contador
sorted() -> organiza a tupla em ordem alfabetica ou númerica, para colocar em ordem precisa tranformar em lista.
.count() -> conta quantas vezes algo em especifico aparece na tupla
.index(value) -> mostra em que posição o value esta
del() -> apaga uma tupla
'''
# ======================================================================

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])

for comida in lanche: # neste tipo não tem como mostrar a posição que a comida esta
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)): # Outra forma de utilizar o for, neste tem como mostra a posição que a comida está
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')

for pos, comida in enumerate(lanche): # neste o enumerate me da tanto o dado (comida) quanto sua posição (pos)
    print(f'Eu vou comer {comida}, na posição {pos}')

print('Comi pra caramba!')

print(sorted(lanche)) # mostra o lanche em ordem alfabetica

# ======================================================================
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b 
d = b + a
print(c,'\n',d)
print(f'Quantas vezes aparece o número 5: {c.count(5)}') # conta quantas vezes o numero 5 aparece na tupla c
print(f'Em qual posição está o número 8: {d.index(8)}') # mostra em qual posição o numero 8 esta
