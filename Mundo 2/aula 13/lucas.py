# forma que o Lucas fez o desafio 53
texto = input('Digite uma frase: ').upper()

tam = (len(texto)-1)
cont = len(texto) / 2
if type(cont) is float:
    cont = cont + 0.5
 
for i in range(int(cont)):
 
    letra_a = texto[i]
    letra_b = texto[tam-i]
 
    if letra_a == letra_b:
        if i+1 == cont:
            print('O texto é palíndromo')
    else:
        print('O texto não é palíndromo')
        break
