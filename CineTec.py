import time

filmes = ['The Batman', 'Velozes e Furiosos 9', 'Doutor Estranho', 'Jogador Número 1']
valores = [34, 17]


def ListarFilmes():
    print('Filmes em cartaz:                      Inteira     Meia\n'
          '--------------------------------------------------------\n'
          '1-{}...........................R${},00...R${},00\n'
          '2-{}........................R${},00...R${},00\n'
          '3-{}......................R${},00...R${},00\n'
          '4-{}...........R${},00...R${},00\n'
          '--------------------------------------------------------\n'
          .format(filmes[0], valores[0], valores[1], filmes[1], valores[0], valores[1],
                  filmes[2], valores[0], valores[1], filmes[3], valores[0], valores[1]))
    time.sleep(3)


def BuscarFilme():
    bscflm = input('Qual filme você esta procurando?\n')
    if bscflm in filmes:
        print('O filme {} está em cartaz no momento'.format(bscflm))
    else:
        print('O filme {}, infelizmente, não esta em cartaz no momento'.format(bscflm))
    time.sleep(3)


def Comprar():
    c = 0
    o = 0
    m = 0
    p = 0
    r = 0

    print('Filmes em cartaz:                      Inteira     Meia\n'
          '--------------------------------------------------------\n'
          '1-{}...........................R${},00...R${},00\n'
          '2-{}........................R${},00...R${},00\n'
          '3-{}......................R${},00...R${},00\n'
          '4-{}...........R${},00...R${},00\n'
          '--------------------------------------------------------\n'
          .format(filmes[0], valores[0], valores[1], filmes[1], valores[0], valores[1],
                  filmes[2], valores[0], valores[1], filmes[3], valores[0], valores[1]))
    c = input('Qual filme você deseja assistir?\n')
    o = int(input('Quantos ingressos são?\n'))
    if o > 1:
        m = int(input('Vocês são estudantes?\n'
              '---------------------\n'
              '  1-Sim       2-Não  \n'
              '---------------------\n'))
    elif o == 1:
        m = int(input('Você é estudante?\n'
              '---------------------\n'
              '  1-Sim       2-Não  \n'
              '---------------------\n'))
    if m == 1:
        if o > 1:
            p = int(input('Quantos ainda estudam?\n'))
        elif o == 1:
            p = 1
        o = o - p
        r = (o * valores[0]) + (p * valores[1])
        print('Sendo {} inteira(s) e {} meia(s), a soma dos ingressos é de R${},00'.format(
            o, p, r
        ))
        time.sleep(5)
        print('O pagamento pode ser efetuado apenas pelo pix\n'
              '---------------------------------------------\n'
              'Chave: 426.356.546-54    Tipo: CPFr\n'
              '---------------------------------------------\n')
        print('Obrigado pela preferência, pode retirar os ingressos.\n')
        time.sleep(5)
    elif m == 2:
        r = (o * valores[0])
        print('Sendo {} inteira(s), a soma dos ingressos é de R${},00'.format(
            o, r
        ))
        time.sleep(5)
        print('O pagamento pode ser efetuado apenas pelo pix\n'
              '---------------------------------------------\n'
              'Chave: 426.356.546-54    Tipo: CPFr\n'
              '---------------------------------------------\n')
        print('Obrigado pela preferência, pode retirar os ingressos.\n')
        time.sleep(5)
    else:
        print('Desculpe mas não foi possível receber sua resposta, tente novamente')

lista = {'Pipoca pequena': 'R$5,00', 'Pipoca média': 'R$10,00', 'Pipoca grande': 'R$15,00', 'Refrigerante': 'R$5,50'}


def listar():
    print(lista)
    time.sleep(3)


def buscar():
    nome = input('Digite o nome do produto: ')
    print(lista.get(nome, "Este produto não consta no catalogo"))
    time.sleep(3)


def adicionar():
    nome = input('Digite o nome do produro a ser cadastrado: ')
    preco = input('Digite o preço do produto: ')
    lista[nome] = preco
    print(lista, '\nCadastro realizado com sucesso!')
    time.sleep(3)


def alterar():
    nome = input('Digite o nome do produto a qual deseja alterar o preco: ')
    if nome in lista:
        precoNovo = input('Digite o novo preço: ')
        lista[nome] = precoNovo
    print(lista.get(nome, "Este produto não consta no catalogo"))
    time.sleep(3)


def listarNomes():
    print('Nomes cadastrados:')
    for nome in lista.keys():
        print(nome)
    time.sleep(5)


x = 0
y = 0
z = 0
while x < 3:
    x = int(input('Escolha para onde deseja ir:\n'
                  '----------------------------\n'
                  'Bilheteria.................1\n'
                  'Lanchonete.................2\n'
                  'Sair.......................3\n'
                  '----------------------------\n'))
    if x == 1:
        while y < 4:
            y = int(input('Escolha uma das funções a seguir:\n'
                          '---------------------------------\n'
                          'Listar..........................1\n'
                          'Buscar..........................2\n'
                          'Comprar.........................3\n'
                          'Sair............................4\n'
                          '---------------------------------\n'))
            if y == 1:
                ListarFilmes()
            elif y == 2:
                BuscarFilme()
            elif y == 3:
                Comprar()
    elif x == 2:
        while z < 6:
            z = int(input('Escolha uma das opções a seguir: \n'
                          '--------------------------------\n'
                          'Listar  .....................  1\n'
                          'Buscar  .....................  2\n'
                          'Adicionar  ..................  3\n'
                          'Alterar  ....................  4\n'
                          'Listar somente Nomes  .......  5\n'
                          'Sair  .......................  6\n'
                          'Obs: digite o Número da opção   \n'
                          '--------------------------------\n'))

            if z == 1:
                listar()
            elif z == 2:
                buscar()
            elif z == 3:
                adicionar()
            elif z == 4:
                alterar()
            elif z == 5:
                listarNomes()

# by Gustavo Wustemberg
# With participation of Gabriel Muller and Laiza Sena