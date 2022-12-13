from abc import ABC, abstractmethod
import pygame

from cringario_util import load_image
from drawable import DrawWithSprite, DrawWithColor
from tiles import Tile
from levels.test_level import platform_size
from bonuses import HealBonus


class BaseWindow(ABC):
    @abstractmethod
    def render(self):
        pass


class StartWindow(BaseWindow):
    def __init__(self, screen):
        self.view = DrawWithColor((0, 0), 900)
        self.menu = pygame.sprite.Group(self.view)
        self.buttons = []
        self.display = screen

    def render(self):
        self.menu.draw(self.display)
        pass
