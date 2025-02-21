nome = input('Digite seu nome completo: ')
nome = nome.title()
print(f'O nome possui Silva: {'Silva' in nome}')

# forma do Guanabara
nome = str(input('Qual é seu nome completo?')).strip()
print(f'Seu nome tem Silva? {'Silva' in nome.lower()}')