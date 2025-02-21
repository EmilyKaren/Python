# leia varios numeros e no final mostre a quantidade de números lidos e a soma dos mesmos, e só pare quando o usuário digitar 999
print('Somatoria de números, caso queira que o programe pare digite 999')
n = cont = soma = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: '))
print(f'O total de números digitados foi: {cont - 1}\nE a soma dos mesmos foi: {soma}')