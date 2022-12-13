import pygame

from drawable import *
from cringario_util import load_image


class Tile(DrawWithSprite):
    sprite = load_image("test2.png")

    def __init__(self, pos, size):
        super().__init__(pos, size, Tile.sprite)

    def update(self, shift):
        self.rect.x += shift

