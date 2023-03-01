import sys, pygame
from math import *

class Player:
    def __init__(self):
        self.direction = None
        self.x = 350
        self.y = 450

        self.plat = pygame.image.load("res/Platform.png").convert_alpha()
        self.rect = self.plat.get_rect()
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def update(self):
        if self.left:
            self.x -= 0
        if self.right:
            self.x += 0

        self.rect.x = self.x
        self.rect.y = self.y

    def render(self, x, y, screen):
        screen.blit(self.plat, self.rect)

class Player:
    def __init__(self):
        self.direction = None
        self.x = 350
        self.y = 450

        self.plat = pygame.image.load("res/Platform.png").convert_alpha()
        self.rect = self.plat.get_rect()
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def update(self):
        if self.left:
            self.x -= 0
        if self.right:
            self.x += 0

        self.rect.x = self.x
        self.rect.y = self.y

    def render(self, x, y, screen):
        screen.blit(self.plat, self.rect)

    def key_down(self, key):
        if key == pygame.K_a:
            self.left = True
        if key == pygame.K_d:
            self.right = True

    def key_up(self, key):
        if key == pygame.K_a:
            self.left = False
        if key == pygame.K_d:
            self.right = False
class Player2:
    def __init__(self):
        self.direction = None
        self.x = 350
        self.y = 15

        self.plat2 = pygame.image.load("res/Platform.png").convert_alpha()
        self.rect2 = self.plat2.get_rect()
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def update(self):
        if self.left:
            self.x -= 0
        if self.right:
            self.x += 0

        self.rect2.x = self.x
        self.rect2.y = self.y

    def render(self, x, y, screen):
        screen.blit(self.plat2, self.rect2)


