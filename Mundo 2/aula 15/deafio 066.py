# leia varios numeros e so pare quando o usuário digitar o numero 999, no final mostre quantos numeros foram digitados e a soma dos mesmos

cont = soma = 0
while True:
    n = int(input('Digite um número [999 faz parar]: '))
    if n != 999:
        soma += n
        cont += 1
    else:
        break
print(f'Foi digitado {cont} números e a soma deles foi {soma}')