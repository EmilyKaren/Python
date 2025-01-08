cidade = input('Digite o nome de uma cidade: ')
cidade = cidade.capitalize()
cidade = cidade.strip()
cidade = cidade.split()
primeiro = cidade[0]
print(f'O nome da cidade começa com Santo? {primeiro == 'Santo'}')

# modo do Guanabara
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
