# valor a ser pago por um produto
print('     Caixa virtual.')
valor = float(input('Informe o valor da compra:\033[1;35mR$ '))
print('\033[mDigite a forma de pagamento baseado na tabela abaixo.\n1 - À vista no dinheiro ou cheque.\n2 - À vista no cartão.\n3 - Em até 2x no cartão.\n4 - 3x ou mais no cartão.\033[1;35m')
pagamento = int(input('Sua escolha: '))
print('\033[m')

if pagamento == 1:
    desconto = valor - ((valor * 10)/ 100)
    print(f'O valor da compra ficará de R$ {desconto:0.2f}')
elif pagamento == 2:
    desconto = valor - ((valor * 5)/ 100)
    print(f'O valor da compra ficará de R$ {desconto:0.2f}')
elif pagamento == 3:
    valor = valor/2
    print(f'A compra será parcelada em 2x de {valor}')
elif pagamento == 4:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    if parcelas >= 3:
        juros = valor * 20 / 100
        vparcela = (valor + juros)/ parcelas
        print(f'A quantidade de juros é de R${juros:0.2f}')
        print(f'A compra será parcelada de {parcelas}x no valor de R${valor + juros:0.2f} dando um total de R${vparcela:0.2f} reais a parcela.')
    else:
        print('Valor incorreto.\nA quantidade de parcelas tem que ser maior ou igual a 3, tente novamente ou escolha outra opção de pagamento.')
else:
    print('Valor digitado incorreto. Verifique se o valor corresponde as opções dadas.')
print('\033[1;35mVolte sempre!\033[m')
