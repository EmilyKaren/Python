nome = str(input('Digite seu nome completo: ')).strip() # remove os espaços antes e depois do nome
print('Análisando seu nome:')
print(f'Em maiúsculas: {nome.upper()}')
print(f'Em minúsculas: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras.') # -> conta a quantidade de letras menos a contagem de quantos espaços tem
print(f'O primeiro nome tem {nome.find(' ')}') # vai contar quantas letras tem antes do delimitador 
