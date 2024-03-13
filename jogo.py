import back
import pygame

pygame.init()
jogo = back.Jogo(640, 480)
jogo.teste()
x = True
while x:
    x = jogo.game_loop()
