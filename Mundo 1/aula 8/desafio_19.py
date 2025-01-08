from random import choice
nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')
lista = [nome1, nome2, nome3, nome4] # no python uma lista fica entre conchetes
sorteio = choice(lista) # choice sorteia alguém aleatório dentro da lista
print(f'Entre os alunos {nome1}, {nome2}, {nome3} e {nome4} foi sorteado:\n{sorteio}!')