from math import trunc
num = float(input('Digite um número flutuante/quebrado: '))
nint = trunc(num)
print(f'O número digitado foi {num} e seu valor inteiro é {nint}')
# trunc -> retorna apenas o número sem suas casas decimais (sem vírgula)