import pygame
import random

W = 640
H = 480


class jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((W, H))
        pygame.display.set_caption("GravWordle")
        self.fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font("assets/font/PressStart2P.ttf", 20)
        return self

    def recebe_eventos(self, asset, estate):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def game_loop(self, window, asset, estate):
        x = self.recebe_eventos(asset, estate)
        t0 = -1
        t = 1
        while x:
            t1 = pygame.time.get_ticks()
            if t0 >= 0:
                t = t1 - t0
            t0 = t1
            asset["fps"] = 1000 / t
            estate["caixa"] += t * estate["vel"]
            if estate["Jx"] <= 0:
                estate["Jx"] = 0
            elif estate["Jx"] >= W - 50:
                estate["Jx"] = W - 50
            for i in range(len(asset["astr"][1][0])):
                if asset["astr"][1][1][i] + 20 >= H:
                    asset["astr"][1][1][i] = 0
                    asset["astr"][1][0][i] = random.randint(0, W)
            self.desenha(window, asset, estate)
            x = self.recebe_eventos(asset, estate)
        return x
