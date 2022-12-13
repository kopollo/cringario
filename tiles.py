import pygame

from drawable import *
from cringario_util import load_image


class Tile:
    sprite = load_image("test2.png")

    def __init__(self, pos, size):
        self.view = DrawWithSprite(pos, size, Tile.sprite)
