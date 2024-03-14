import pygame
import random
import json


class caixa:
    def __init__(self):
        self.width = 300
        self.height = 150
        self.vel = 1
        self.fonte = pygame.font.Font("assets/font/PressStart2P.ttf", 20)
        self.pal = self.fonte.render(self.get_word("1"), True, (0, 0, 0))
        self.pos = [random.randint(0, 900), -100]
        self.ret = self.pal.get_rect(center=(self.pos[0] + 150, self.pos[1] + 40))
        self.text = ""
        self.R = self.fonte.render(self.text, True, (255, 255, 255))
        # self.retR = self.R.get_rect(center=(self.pos[0] + 150, self.pos[1] + 140))

    def desenha(self, img):
        caixa = pygame.image.load(img)
        caixa = pygame.transform.scale(caixa, (self.width, self.height))
        return caixa

    def get_word(self, level):
        with open("assets/words.json", "r") as j:
            contents = json.loads(j.read())
        number = str(random.randint(1, 10))
        # print(contents[level][number])
        return contents[level][number]

    def update(self):
        r = self.fonte.render(self.text, True, (255, 255, 255))
        self.pos[1] += self.vel
        # if self.C.pos[1] > self.height + 10:
        if self.pos[1] >= 800:
            if self.pal != r:
                self.vel += 0.1
            self.pos[0] = random.randint(0, 900)
            self.pal = self.fonte.render(self.get_word("1"), True, (0, 0, 0))
            self.text = ""
            self.pos[1] = -100
            print(self.vel)


class Jogo:

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.vidas = 3
        self.C = caixa()
        #  self.retR = self.text.get_rect(center=(self.pos[0] + 150, self.pos[1] + 100))

        pygame.display.set_caption("GravWorddle")

    def recebe_eventos(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_BACKSPACE
                and len(self.C.text) >= 0
            ):
                self.C.text = self.C.text[:-1]
                print(self.C.text)
            elif event.type == pygame.KEYDOWN:
                self.C.text += str(event.unicode)

        return True

    def desenha(self):
        self.window.fill((255, 0, 0))
        R = self.C.fonte.render(self.C.text, True, (255, 255, 255))
        self.window.blit(
            self.C.desenha("assets/imgs/img.png"),
            (self.C.pos[0], self.C.pos[1]),
        )
        self.window.blit(self.C.pal, (self.C.pos[0] + 100, self.C.pos[1] + 30))
        # self.window.blit(self.R, self.C.retR)
        self.window.blit(R, (self.C.pos[0] + 110, self.C.pos[1] + 100))
        pygame.display.flip()

    def game_loop(self):
        x = Jogo.recebe_eventos
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        while x:
            caixa.update(self.C)
            Jogo.desenha(self)
            # caixa.desenha()
            x = Jogo.recebe_eventos(self)
            # caixa.update(self.C)
        return x
