import pygame
import random


class caixa:
    def __init__(self, width):
        self.width = width
        self.vel = 0.3
        self.fonte = pygame.font.Font("assets/font/PressStart2P.ttf", 5)
        self.pal = self.fonte.render("palavra", True, (0, 0, 0))
        self.caixa = self.pal.get_rect()
        # pygame.transform.scale(pygame.image.load("assets/img/caixa,png"), (20, 10))
        self.pos = [random.randint(0, self.width), -30]
        # self.fonte_padrao = pygame.font.get_default_font()
        print("Entrou")

    # def events(self):
    #     if Jogo.recebe_eventos(self) == True:
    #         caixa.pos[1] += caixa.vel
    #     return True

    def desenha(self):
        # rectI = self.C.pal.get_rect()
        # pygame.draw.rect(caixa.pal, (255, 0, 0), rectI, 10)
        pass


class Jogo:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.vidas = 3
        self.C = caixa(self.width)

    def teste(self):
        pygame.display.set_caption("GravWorddle")

    def recebe_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        self.C.pos[1] += self.C.vel
        if self.C.pos[1] > self.height:
            self.C.pos[1] = -10
        return True

    def desenha(self):
        print("entroi desenha")
        self.window.fill((255, 255, 255))
        caixa.desenha(self)
        # self.window.blit(self.C.caixa, (self.C.pos[0], self.C.pos[1]))
        self.window.blit(self.C.pal, (self.C.pos[0], self.C.pos[1] - 10))
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
