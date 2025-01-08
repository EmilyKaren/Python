# h²=c²+c²
import math
ca = float(input('Informe o cateto adjacente: '))
co = float(input('Informe o cateto oposto: '))
h = math.hypot(ca, co)
print(f'O valor da hipotenusa é {h:.2f}.')