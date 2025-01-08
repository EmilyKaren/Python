a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))
if a+b > c and b+c > a and a+c > b:
    print(f'PODE formar um triângulo com as medidas {a}, {b}, e {c}.')
else:
    print(f'NÃO PODE formar um triângulo com os número {a}, {b} e {c}.')
    