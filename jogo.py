import back

# import pygame

jogo = back.Jogo(1200, 800)
screen = back.telafinal(jogo, 1200, 800)
x = 1
while x == 1 or x == 2:
    while x == 1:
        # while jogo.tela == 1:
        x = jogo.game_loop()
        # x = screen.telafinal()
        # print("saiu")
    while x == 2:
        x = screen.telafinal(x)
