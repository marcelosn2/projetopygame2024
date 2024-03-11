import pygame
import random

W = 640
H = 480


class caixa:
    def __init__(self):
        self.vel = 2
        self.caixa = pygame.transform.scale(
            pygame.image.load("assets/img/caixa,png"), (20, 10)
        )
        self.pos = (random.randint(0, W), -30)

    def events(self):
        if jogo.recebe_eventos() == True:
            self.pos[1] += self.vel
            return True

    def desenha(self):
        for i in caixas
        self.window.blit(self.caixa, self.pos)


class jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((W, H))
        pygame.display.set_caption("GravWordle")
        self.fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font("assets/font/PressStart2P.ttf", 20)
        return self

    def recebe_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def desenha(self):
        self.window.fill(0, 0, 0)

    def game_loop(self):
        x = jogo.recebe_eventos(self)
        t0 = -1
        self.t = 1
        while x:
            t1 = pygame.time.get_ticks()
            if t0 >= 0:
                self.t = t1 - t0
            t0 = t1

            self.desenha()
            caixa.desenha()
            x = self.recebe_eventos()
        return x
