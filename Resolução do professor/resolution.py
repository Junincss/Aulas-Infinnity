import random

escolhas = ["pedra", "papel", "tesoura"]

def computador(escolhas):
    return random.choice(escolhas)

def jogador(escolhas):
    jogada = int(input('Digite uma das opções:\n'
                       "1 - pedra\n"
                       "2 - papel\n"
                       "3 - tesoura"))
    
    return escolhas[jogada - 1]

def jogo(computador, jogador):
    if jogador == computador:
        print("Empate")
    elif((jogador == "pedra" and computador == "tesoura") or 
         (jogador == "tesoura" and computador == "papel") or 
         (jogador == "papel" and computador == "pedra")):
        print("Jogador Venceu")
    else:
        print("Computador Venceu")

'''jj = jogador(escolhas)
jc = computador(escolhas)

jogo(jc, jj)'''

jogo(computador(escolhas), jogador(escolhas))