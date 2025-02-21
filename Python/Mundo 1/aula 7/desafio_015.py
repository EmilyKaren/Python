# R$60 o dia, R$0.15 por Km rodado
d = int(input('Quantos dias o carro ficou alugado: '))
km = float(input('Quantos quilômetros o carro percoreu: '))
vd = d*60
vkm = km*0.15
vt = vd+vkm
print(f'Considerando que o valor do dia é R${vd:0.2f} e o valor rodado foi de R${vkm:0.2f} o valor total é de R${vt:0.2f}')