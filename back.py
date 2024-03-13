import pygame
import random


class caixa:
    def __init__(self, width, height):
        self.width = width
        self.vel = 2
        self.caixa = self.pal.get_rect()
        # pygame.transform.scale(pygame.image.load("assets/img/caixa,png"), (20, 10))
        self.pos = (random.randint(0, self.width), -30)
        self.pal = self.fonte.render("palavra", True, (0, 0, 0))
        # self.fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font("assets/font/PressStart2P.ttf", 20)
        print("Entrou")

    def events(self):
        # if jogo.recebe_eventos(self) == True:
        # caixa.pos[1] += caixa.vel
        return True

    def desenha(self):
        rectI = self.pal.get_rect()
        pygame.draw.rect(self.pal, (255, 0, 0), rectI, 10)


class Jogo:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.vidas = 3
        # caixa()

    def teste(self):
        pygame.display.set_caption("GravWorddle")

    def recebe_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        caixa.events(self)
        return True

    def desenha(self):
        print("entroi desenha")
        self.window.fill(255, 255, 255)
        # caixa.desenha()
        # self.window.blit(caixa.caixa, (caixa.pos[0], caixa.pos[1]))
        # self.window.blit(caixa.pal, (caixa.pos[0], caixa.pos[1] - 10))
        pygame.display.flip()

    def game_loop(self):
        x = Jogo.recebe_eventos
        t0 = -1
        print("Entrou game loop")
        while x:
            t1 = pygame.time.get_ticks()
            if t0 >= 0:
                t = t1 - t0
            t0 = t1

            Jogo.desenha(self)
            # caixa.desenha()
            x = Jogo.recebe_eventos(self)
        return x
