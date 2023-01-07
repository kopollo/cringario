import pygame

from drawable import *
from cringario_util import load_image


class Ground(DrawWithSprite):
    def __init__(self, pos, size, img):
        self.sprite = load_image(img)
        super().__init__(pos, size, self.sprite)

    def update(self, shift_x):
        self.rect.x += shift_x