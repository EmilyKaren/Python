# A=b*al
# 1L tinta = 2m²
b = float(input('Digite a largura da parede:'))
al = float(input('Digire a altura da parede:'))
a = b*al
print(f'A área da parede é {a:0.2f}m²')
t = a/2
print(f'A quantidade de tinta necessária é de {t:0.3f} litros.')