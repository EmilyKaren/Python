from math import radians, sin, cos, tan
a = float(input('Digite um ângulo: '))
an = radians(a) # transformar o número em ângulo
sen = sin(an)
cos = cos(an)
tang = tan(an)
print(f'O valor do seno é {sen:0.2f}, do coseno é {cos:0.2f} e da tangente é {tang:0.2f}')