# contagem regressiva de 10 a 0 com uma pausa de 1 segundo entre eles

from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('🎊🎆🎉\033[1;33mFeliz Ano Novo!!!!\033[m🎊🎆🎉')
