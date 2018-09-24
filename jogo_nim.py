'''
Jogo Nim.
V. 003

Arrumar computador_escolhe_jogada()
O resultado dos testes com seu programa foi:

***** [0.11 pontos]: Testando se computador_escolhe_jogada usa a estratégia vencedora (n = 14, m = 4) -
Falhou ***** AssertionError: Esperado: 4; recebido: 1 computador_escolhe_jogada deve usar a estratégia
vencedora e devolver o número de peças que o computador vai remover nessa jogada.



***** [0.11 pontos]: Testando se computador_escolhe_jogada usa a estratégia vencedora (n = 13, m = 4) -
Falhou ***** AssertionError: Esperado: 3; recebido: 1 computador_escolhe_jogada deve usar a estratégia
vencedora e devolver o número de peças que o computador vai remover nessa jogada.

'''

def campeonato():
  print("\nVoce escolheu um campeonato!")
  usuario = 0
  computador = 0
  p=0
  i = 0
  while i < 3:
    print("\n**** Rodada", i + 1, "****\n")
    p = partida()
    if p == 1:
      usuario = usuario + p
    else:
      computador = computador + 1
    i += 1

  print("\n**** Final do campeonato! ****")

  print("\nPlacar: Você", usuario, "X", computador, "Computador")


def computador_escolhe_jogada(n,m):
  x = m
  while x > 0:
    if (n-x) % (m+1) == 0:
      print("1",x)
      break
    else:
      x = x - 1
      print("11",x)

  if x == 0:
    x = m
    print("2",x)

  if x > n:
    x = n
    print("3",x)

  
  if x == 1:
    print("\nO computador tirou uma peça")
  else:
    print("\nO computador tirou", x, "peças")
  return x
  

def usuario_escolhe_jogada(n,m):
  x = 0
  while x>m or x<1 or x > n:
    x = int(input("\nQuantas peças você vai tirar? "))
    if x>m or x<1 or x > n:
      print("\nOops! Jogada inválida! Tente de novo.")
  if x == 1:
    print("\nVocê tirou uma peça.")
  else:
    print("\nVocê tirou", x, "peças")
  return x


def partida():
  

  
  n = int( input("Quantas peças? ")  )
  m = int( input("Limite de peças por jogada? ")  )

  if n % (m+1) == 0:
    print("\nVocê começa!")
    quemjoga = True
  else:
    print("\nComputador começa!") # verificar isso
    quemjoga = False

  while n > 0:
    if quemjoga == True:
      n = n - usuario_escolhe_jogada(n,m)
      if n == 0:
        print("Fim do jogo! Você ganhou!")
        p = 1
        return p
      else:
        if n == 1:
          print("Agora restam uma peça no tabuleiro.")
        else:
          print("Agora restam", n ,"peças no tabuleiro.")
      quemjoga = False
    else:
      k = computador_escolhe_jogada(n,m)
      n = n - k
      if n == 0:
        print("Fim do jogo! O computador ganhou!")
      else:      
        if n == 1:
          print("Agora restam uma peça no tabuleiro.")
        else:
          print("Agora restam", n ,"peças no tabuleiro.")
      quemjoga = True      
    

print("Bem-vindo ao jogo do NIM! Escolha:\n")
tipo = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato"))
if tipo == 1:
  partida()
else:
  campeonato()

'''

'''
