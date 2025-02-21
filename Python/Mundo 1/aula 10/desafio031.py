km = float(input('Digite quantos quilômetros tem sua viagem: '))
if km <= 200:
    v = km*0.50
else:
    v = km*0.45
print(f'O valor da pasagem será de R${v:0.2f}')
print('Boa viagem!')

''' forma simplificada - Guanabara '''

km = float(input('Digite quantos quilômetros tem sua viagem: '))
'''operador ternario'''
v = km * 0.50 if km <= 200 else km * 0.45
print(f'O valor da pasagem será de R${v:0.2f}')
print('Boa viagem!')
