# digite sete números e os coloque em uma lista sendo que dentro desta lista tem que ter uma lista par e uma lista impar, depois mostre os numeros impar e par em ordem crescente

numeros = [[], []]
dado = 0
for c in range(0, 7):
    dado = (int(input(f'Digite {c+1}º número: ')))
    if dado % 2 == 0:
        numeros[0].append(dado)
    else:
        numeros[1].append(dado)
# print(numeros)
par = numeros[0]
impar = numeros[1]
par.sort()
impar.sort()
print(f'Os números pares foram: {par}')
print(f'Os números ímpares foram: {impar}')
