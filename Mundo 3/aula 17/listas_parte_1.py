# Váriaveis Compostas [LISTAS]
'''
As listas são Mutáveis
    Caso você faça com no exemplo 3 e acha que vai adicionar o 8 apenas na lista B está errado, muda nas duas, isso porque quando diz que b = a você faz uma ligação entre as listas.
.append() -> adiciona um item no final da lista 
.insert(posição, 'item adicionar') -> adiciona um item na posição escolhida
del lista[3] -> apaga o item da lista na posição 3
.pop[3] -> apaga o item da lista na posição 3 *normalmente utilizado para apagar o ultimo item da lista
.remove('item remover') ->  apaga o valor da lista * elimina pelo conteudo
list() -> cria uma lista
.sort() -> organiza os valores dentro da lista
.sort(reverse=True) -> os valores ficam ordenados na ordem contraria
len(lista) -> mostra quantos elementos tem dentro da lista
find() -> Procura os caracteres escolhido
rfind() -> começa a busca no final da frase
.index(value) -> mostra em que posição o value esta
'''
# exemplo 1
num = [2, 5, 9, 4]
print(f'Lista = {num}')
num[2] = 3
num.append(7)
print(f'Adicionei o 7 e troquei o número da 3ª posição {num}')
num.sort()
print(f'Ordenados {num}')
num.sort(reverse=True)
print(f'Ordem reversa {num}')
num.insert(3, 0)
print(f'Inseri o número 0 na 4ª posição: {num}')
num.pop()
print(f'Tirei o último número {num}')

# exemplo 2
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
# valores.append(6)
# valores.append(8)
# valores.append(12)
for c, v in enumerate(valores):
    print(f'Na posição {c} eu encontrei o valor {v}!')
print('Cheguei ao final da lista.')

# exemplo 3
a = [2, 3, 4, 7]
b = a # fez uma ligação
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 3, 4, 7]
b = a[:] # cria uma copia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')