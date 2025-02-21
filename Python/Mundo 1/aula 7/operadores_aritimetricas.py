# Operadores aritimétricas
    # + adição, 5+2 == 7
    #  - subtração, 5-2 == 3
    # * multipplicação, 5*2 == 10
    # / divisão, 5/2 == 2,5
    # ** potência, 5**2 == 25
    # // divisão inteira,[divide sem utilizar virgula] 5//2 == 2
    # % resto da divisão,[é o resto que sobrou da divisão inteira] 5%2 == 1
    # n**(1/2) ou pow(n,(1/2)) raiz quadrada

# Ordem de precedência
    # 1- ()
    # 2- **
    # 3- *, /, //, %
    # 4- +, -

nome = input('Qual seu nome?')
print(f'Prazer em te conhecer {nome:¨^20}!') 
# se colocar :20 a str nome vai ser posicionada entre 20 caracteres se colocar qualquer simbolo ante do número ele vai preencher o espaço "vazio".
# Para fazer um valor float ter uma determinada quantidade de casas decimais basta colocar :0.2f o 0.2 é quantas casas decimais o valor vai ter e o f pois é um float.
# ^ -> centraliza
# < -> posiciona à direita
# > -> posiciona à esquerda
# \n -> quebra a linha