import back

# import pygame

jogo = back.Jogo(1200, 800)
screen = back.telafinal(1200, 800)
x = True
while x:
    if jogo.tela != 1:
        x = screen.telafinal(jogo, jogo.tela)
    else:
        x = jogo.game_loop()
