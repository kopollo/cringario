from abc import ABC, abstractmethod
import pygame

from cringario_util import load_image
from drawable import DrawWithSprite, DrawWithColor
from tiles import Tile
from levels.test_level import platform_size
from bonuses import HealBonus
import buttons as button


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


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
start_img = pygame.image.load('').convert_alpha()
exit_img = pygame.image.load('').convert_alpha()
result_table_img = pygame.image.load('').convert_alpha()
start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)
resultbutton = button.Button(450, 200, result_table_img, 0.8)