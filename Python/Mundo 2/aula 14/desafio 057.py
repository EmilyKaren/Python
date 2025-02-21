# Leia o sexo de uma pessoa, mas só aceita os valores M ou F. Caso o valor esteja errado peça para digitar novamente até acertar

sexo = ''
print('\033[1m===== Coleta de Dados =====\033[m')
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite seu sexo [M/F]:\033[1;33m ')).strip().upper()[0]
    if sexo != 'F' and sexo != 'M':
        print('\033[mO texto foi digitado incorretamente. Tente novamente!')
        print('-'* 40)
print('\033[mFim')
print('\033[1m=\033[m'* 40)

# forma do guanabara

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
