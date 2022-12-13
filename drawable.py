import os
import sys

import pygame


class DrawWithColor(pygame.sprite.Sprite):
    def __init__(self, pos, size, color='grey'):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)


class DrawWithSprite(pygame.sprite.Sprite):
    def __init__(self, pos, size, image):
        super().__init__()
        image = pygame.transform.scale(image, (size, size))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


class DrawWithText(pygame.sprite.Sprite):
    def __init__(self, pos, size, text):
        super().__init__()
        font = pygame.font.Font(None, 50)
        self.textSurf = font.render(text, True, (100, 255, 100))
        self.image = pygame.transform.scale(self.textSurf, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        # self.image.blit(self.textSurf, [W / 2 - W / 2, H / 2 - H / 2])
        # if we wanna size of text, not fixed