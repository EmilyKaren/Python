# fatiamento
    # frase[9] Pega os caracteres da posição indicada
    # frase[9:13] -> Pega os caracteres das posições indicadas
    # frase[9:18:2] -> Pega os caracteres das posições indicadas pulando 2
# Análise
    # len() -> Mostra quantas letras tem a frase -> len(frase) = 38 letras
    # count() -> Conta quantas vezes aparece a letra escolhida -> frase.count('s')
        #frase.count('o',0,13) -> fatiamento + analise
    # find() -> Procura os caracteres escolhido -> frase.find('aprendendo')
        # rfind() -> começa a busca no final da frase -> frase.rfind('aprendendo')
# transformação
    # replace() -> Troca uma palavra por outra na frase -> frase.replace('python','JavaScript')
    # upper() -> Colocar todas as outras letras em maiúsculo -> frase.upper()
    # lower() -> Colocar todas as outras letras em minusculo -> frase.lower()
    # capilalize() -> Coloca todas a frase em minusculo menos a 1 letra -> frase.capitalize()
    # title() -> Todas as palavras começa com letra maiúscula -> frase.title()
    # strip() -> Tira o espaço do começo e no fim da frase -> frase.strip()
        # frase.rstrip() -> remove apenas os espaços da direita (ultimos espaços)
        #frase.lstrip() -> remove apenas os espaços da esquerda (primeiros espaços)
# divisão
    # split() -> Vai ocorrer uma divisão entre os espaços da frase -> frase.split()
# junção
    # .join() -> Juntar uma coisa com a outra -> '-'.join.(frase) Estou-aprendendo-a-programar-em-python
