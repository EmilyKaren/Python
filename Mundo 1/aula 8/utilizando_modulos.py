# import bebida -> importa todos os tipos de bebidas
# from bebida import sprit -> importa apenas a bebida que eu escolho
# from bebida import sprit, coca cola -> para importar mais de uma basta usar a vírgula.
# python.org site com todas as bibliotecas
# math -> biblioteca matemática
# random -> gera números aleatorios
# ctrl + espaço -> mostra todas as bibliotecas ou opções que você pode colocar

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {math.ceil(raiz)}') # ceil -> arredonda para cima

from math import sqrt 
num = int(input('Digite um número: '))
raiz = sqrt(num) # quando importo algo especifico não preciso colocar o math.alguma coisa. É so escrever direto.
# a vantagem de usar esse modo é que ocupa menos espaço, podendo fazer o cód. rodar mais rápido
print(f'A raiz quadrada de {num} é {math.ceil(raiz)}')

import random
num = random.random() # -> mostra um número aleatorio entre 0 e 1 (float)
num1 = random.randint(0, 10) # -> randomizar um número int entre os que você colocou
print(f'num')
print(f'num1')
