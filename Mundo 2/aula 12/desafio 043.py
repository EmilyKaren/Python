# calcular o imc de uma pessoa
from time import sleep
print('=*=' *20)
print('Calculadora de IMC [Índice de Massa Corporal].')
peso = float(input('Digite qual é o seu peso: '))
altura = float(input('Informe sua altura: '))
print('\033[1;90mCalculando...\033[m')
sleep(2)
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Você esta \033[33mabaixo do peso\033[m. Seu IMC foi de {imc:0.2f}')
elif imc > 18.5 and imc < 25:
    # 18.5 <= imc < 25 outra forma de representar
    print(f'Você esta no \033[32mpeso ideal\033[m. Seu imc foi de {imc:0.2f}')
elif imc > 25 and imc < 30:
    print(f'Você está com \033[34msobrepeso\033[m. Seu imc foi de {imc:0.2f}')
elif 30 <= imc < 40:
    print(f'Você está com \033[31mobesidade\033[m. Seu imc foi de {imc:0.2f}')
else:
    print(f'\033[1;31;43mVocê esta apresentando obesidade morbida\033[m. Seu IMC foi de {imc:0.2f}')
print('=*=' *20)
