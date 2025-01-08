# leia 5 valores e os coloque em uma lista ja na posiçao correta
'''
# peguei com o chat GPT, não consegui fazer
lista = []
nova = []
for p in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

for valor in lista:
    posicao_inserir = 0
    # Encontre a posição correta
    while posicao_inserir < len(nova) and nova[posicao_inserir] < valor:
        posicao_inserir += 1
    # Insira o valor na posição correta
    nova.insert(posicao_inserir, valor)

print("Lista original:", lista)
print("Lista ordenada:", nova)
'''
#forma guanabara

lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados foram {lista}')
