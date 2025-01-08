v = float(input('Qual a velocidade do seu carro? '))
if v <= 80:
    print('Você esta na velocidade permitida. Parabens!')
else:
    m = (v-80)*7
    print(f'Você ultrapassou a velocidade permitida de 80km e terá que pagar uma multa de R${m:0.2f} reais.')