import back
import pygame

jogo = back.Jogo(1200, 700)
x = True
while x:
    x = jogo.game_loop()
