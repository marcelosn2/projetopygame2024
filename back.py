import pygame
import random
import json


class caixa:
    def __init__(self):
        self.width = 300
        self.height = 100
        self.vel = 1
        self.fonte = pygame.font.Font("assets/font/PressStart2P.ttf", 20)
        self.FONTE = pygame.font.Font("assets/font/PressStart2P.ttf", 50)
        self.pal = self.get_word("1")
        self.pos = [random.randint(0, 900), -100]
        self.text = ""
        self.point = 0
        self.win = pygame.mixer.Sound("assets\snd\pew.wav")
        self.boom = pygame.mixer.Sound("assets\snd\expl3.wav")

    def desenha(self, img):
        caixa = pygame.image.load(img)
        caixa = pygame.transform.scale(caixa, (self.width, self.height))
        return caixa

    def get_word(self, level):
        with open("assets/words.json", "r") as j:
            contents = json.loads(j.read())
        number = random.randint(1, 50)
        # print(contents[level][number])
        return contents[level][number]

    def update(self, x, jogo):
        self.pos[1] += self.vel
        self.point = 0

        if self.pos[1] >= 800:
            if self.pal != self.text:
                # print("entrou")
                self.vel += 1
                self.point = -10
                jogo.vidas -= 1
                self.boom.play()
            else:
                self.vel = 1
            if x > 500:
                self.pal = self.get_word("3")
            elif x > 100:
                self.pal = self.get_word("2")
            else:
                self.pal = self.get_word("1")
            self.pos[0] = random.randint(0, 900)
            self.text = ""
            self.pos[1] = -100
            # print(self.vel)
        if len(self.pal) == len(self.text):
            if self.pal == self.text:
                self.point = 1
                self.vel = 10
                self.win.play()
        # if self.vida==0:

        return self.point


class Jogo:

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.pontos = 0
        self.vidas = 3
        self.tela = 1
        self.C = caixa()
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
                # print(self.C.text)
            elif event.type == pygame.KEYDOWN:
                self.C.text += str(event.unicode)
        if self.vidas <= 0:
            self.tela = 0
            return False
        return True

    def desenha(self):
        self.window.fill((255, 0, 0))
        self.window.blit(self.C.FONTE.render(self.heart, True, (0, 0, 0)), (10, 10))
        self.window.blit(
            self.C.desenha("assets/imgs/img.png"),
            (self.C.pos[0], self.C.pos[1]),
        )
        self.window.blit(
            self.C.fonte.render((self.C.pal), True, (0, 0, 0)),
            (self.C.pos[0] + 100, self.C.pos[1] + 10),
        )
        # self.window.blit(self.R, self.C.retR)
        self.window.blit(
            (self.C.fonte.render(self.C.text, True, (255, 255, 255))),
            (self.C.pos[0] + 110, self.C.pos[1] + 80),
        )
        self.window.blit(
            (self.C.FONTE.render(str(self.pontos), True, (255, 255, 255))),
            (1000, 10),
        )
        # self.window.blit(self.C.fonte.render("1", True, (255, 255, 255))(10, 10))
        pygame.display.flip()

    def sum_point(self, point):
        self.pontos += point

    def game_loop(self):
        x = Jogo.recebe_eventos
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        while x:
            caixa.update(self.C, self.pontos, self)
            self.heart = chr(9829) * self.vidas
            Jogo.desenha(self)
            self.sum_point(self.C.point)
            # caixa.desenha()
            x = Jogo.recebe_eventos(self)
            # caixa.update(self.C)
        return x


class telafinal:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))

    def telafinal(self, jogo, n):

        if n != 1:
            jogo.window.fill((0, 0, 0))
            jogo.window.blit(
                (jogo.C.FONTE.render(str(jogo.pontos), True, (255, 255, 255))),
                (self.width / 2, self.height / 2),
            )
            jogo.window.blit(
                (
                    jogo.C.FONTE.render(
                        "press space to go again",
                        False,
                        (255, 255, 255),
                    )
                ),
                ((self.width / 2, (self.height / 2) + 20)),
            )
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return 1
        return True
