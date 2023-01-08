from abc import ABC, abstractmethod

import pygame

from drawable import DrawWithSprite
from cringario_util import load_image


class WinObject(DrawWithSprite):
    cup = load_image("win.png")

    def __init__(self, pos, size):
        super().__init__(pos, size, WinObject.cup)

    def update(self, shift):
        self.rect.x += shift
