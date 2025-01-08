# Condição:
# if carro.esquerda():
#   bloco True
# else:
#   bloco False
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo.')
else:
    print('Carro velho.')
print('--FIM--')

# Condição simplificada: [não muito indicada]
tempo = int(input('Quantos anos tem seu carro?'))
print(f'Carro novo'if tempo<=3 else'Carro velho')
print('--FIM--')

# quando tem o else é uma condicional composta, quanto tem apenas o if é uma condição simples
