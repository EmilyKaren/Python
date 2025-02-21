# crie uma tupla com os 20 primeiros no campeonato brasileiro de futebol e depois mostre:
# a) apenas os 5 primeiros colocados
# b) os ultimos 4 colocados da tabela
# c) os times em ordem alfaetica
# d) em que posição esta o time chapecoense

time = ('Botafogo', 'Palmeiras', 'Flamengo','Fluminense','Atlético Mineiro','Grêmio','São Paulo','Corinthians','Internacional','Santos','Red Bull Bragantino','Athletico Paranaense','Cruzeiro','Vasco da Gama','Goiás','Cuiabá','Bahia','Atlético Goianiense','Fortaleza','América Mineiro')

print(f'Os 5 primeiros colocados foram: {time[:5]}')
print('='*80)
print(f'Os últimos 4 colocados foram: {time[-4:]}')
print('='*80)
print(f'Os times em ordem alfabética: {sorted(time)}')
print('='*80)
print(f'O Cruzeiro ficou na {time.index('Cruzeiro') + 1}ª posição')
print('='*80)
