# separar os nomes de uma string

from time import sleep

lista_de_nomes = 'SIDNEI ROGERIO DOS SANTOS, ROBERTO FARIA, MARCELO FONTANA MAGALHAES, ANDRE LUIZ DA SILVA, WILLIAN APARECIDO DIONISIO, DOUGLAS LUIZ DUTRA'
palavras = lista_de_nomes.split(",")
for i, nome_completo in enumerate(palavras):
    nome = nome_completo.split()
    primeiro = nome[0]
    resto = ' '.join(nome[1::])
    print(f'Pessoa {i + 1} - Nome {primeiro} Sobrenome {resto}')
    sleep(2)
