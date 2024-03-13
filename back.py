import pygame
import random


class caixa:
    def __init__(self):
        self.width = 300
        self.height = 150
        self.vel = 1.3
        self.fonte = pygame.font.Font("assets/font/PressStart2P.ttf", 20)
        self.pal = self.fonte.render("palavra", True, (0, 0, 0))
        self.pos = [random.randint(0, 900), -30]
        self.ret = self.pal.get_rect(center=(self.pos[0] + 150, self.pos[1] + 40))
        self.text = ""
        self.R = self.fonte.render(self.text, True, (255, 255, 255))
        self.retR = self.pal.get_rect(center=(self.pos[0] + 150, self.pos[1] + 140))

    def desenha(self, img):
        caixa = pygame.image.load(img)
        caixa = pygame.transform.scale(caixa, (self.width, self.height))

        return caixa

    def update(self):
        pass


class Jogo:

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.vidas = 3
        self.C = caixa()
        self.clock = pygame.time.Clock()
        #  self.retR = self.text.get_rect(center=(self.pos[0] + 150, self.pos[1] + 100))

        pygame.display.set_caption("GravWorddle")

    def recebe_eventos(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_BACKSPACE
                and len(self.text) >= 0
            ):
                self.text = self.text[:-1]
                print(self.text)
            elif event.type == pygame.KEYDOWN:

                self.C.text += str(event.unicode)
                print(self.text)
                # pass
        self.C.pos[1] += self.C.vel
        if self.C.pos[1] > self.height:
            self.C.pos[1] = -10
        return True

    def desenha(self):
        self.window.fill((255, 255, 255))
        self.window.blit(
            self.C.desenha("assets/imgs/img.png"),
            (self.C.pos[0], self.C.pos[1]),
        )
        self.window.blit(self.C.pal, (self.C.pos[0] + 90, self.C.pos[1] + 30))
        # self.window.blit(self.R, self.C.retR)
        self.window.blit(self.C.R, (self.C.pos[0] + 150, self.C.pos[1] + 40))
        pygame.display.flip()

    def game_loop(self):
        x = Jogo.recebe_eventos
        self.clock.tick(60)

        while x:

            Jogo.desenha(self)
            # caixa.desenha()
            x = Jogo.recebe_eventos(self)
        return x
