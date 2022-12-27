from abc import ABC, abstractmethod

import pygame

from drawable import DrawWithSprite
from cringario_util import load_image


class BaseBonus(ABC, pygame.sprite.Sprite):
    @abstractmethod
    def add_bonus(self, player):
        pass

    def hide_bonus(self):
        self.kill()

    def update(self, shift):
        self.rect.x += shift


class HealBonus(BaseBonus, DrawWithSprite):
    BONUS_HP = 1
    BONUS_SCORE = 50
    image = load_image("cat.png")

    def __init__(self, pos, size):
        super().__init__(pos, size, HealBonus.image)
        self.hp = HealBonus.BONUS_HP
        self.score = HealBonus.BONUS_SCORE

    def add_bonus(self, player):
        player.add_score(self.score)
        player.add_hp(self.hp)


class SimpleBonus(BaseBonus, DrawWithSprite):
    BONUS_SCORE = 100
    image = load_image("cat2.png")

    def __init__(self, pos, size):
        super().__init__(pos, size, SimpleBonus.image)
        self.score = SimpleBonus.BONUS_SCORE

    def add_bonus(self, player):
        player.add_score(self.score)
