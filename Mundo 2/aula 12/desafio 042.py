# se as retas tiverem como formar um triangulo informe qual o tipo de triangulo
a = float(input('Infome o valor da primeira reta: '))
b = float(input('Informe o valor da segunda reta: '))
c = float(input('Informe o valor da terceira reta: '))
if a+b > c and b+c > a and a+c > b:
    print(f'Tem como fazer um triângulo com as retas {a}, {b} e {c}.')
    if a != b and b != c and c != a:
     # a != b != c != a:
        print('E seu tipo de triângulo é: \033[4mEscaleno!\033[m')
    elif a == b != c or b == c != a or c == a != b:
        print('E seu tipo de triângulo é: \033[4mIsósceles!\033[m')
    elif a == b and b == c and c == a:
       # a == b == c outra formar de fazer
        print('E seu tipo de triângulo é: \033[4mEquilátero!\033[m')
else:
    print(f'Não tem como formar um triângulo com os valores {a}, {b} e {c}.')
