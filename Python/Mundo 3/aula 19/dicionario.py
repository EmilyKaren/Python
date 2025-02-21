'''
tuplas -> ()
listas -> []
dicionarios -> {}

Pode dizer que é um dicionário de duas formas
1. dict()       2. {}

Em dicionários .append() não funciona, para criar um novo item basta fazer:
dados['sexo'] = 'M'

Para remover elementos basta usar o del
del dados['idade']

dados.values() -> me mostra os valores (Pedro, 25)
dados.keys() -> mostra as chaves (nome, idade)
dados.items() -> mostra os dois (nome: Pedro, idade: 25)

.copy() -> copia os itens de um dicionario para uma lista
'''
dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'M'
print(dados['sexo'])
print('='*40)

filme = {'titulo':'StarWars',
        'ano':1977,
        'diretor':'George Lucas'
        }
print(filme.values())

for k,v in filme.items():
    print(f'O {k} é {v}')

# k = keys
# v = values
print('='*40)

pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22,
    }
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
pessoas['peso'] = 98.5
for v in pessoas.values():
    print(v)
print('='*40)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print('='*40)

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)

for e in brasil: # referente aos valores da lista
    for k, v in e.items(): # referente aos valores do dicionario
        print(f'O campo {k} tem o valor {v}')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
