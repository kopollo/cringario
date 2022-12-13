from abc import ABC, abstractmethod
from drawable import DrawWithSprite
from cringario_util import load_image


class BaseBonus(ABC):
    def __init__(self, pos, size, sprite):
        pass

    @abstractmethod
    def is_collected(self):
        pass

    @abstractmethod
    def add_bonus(self):
        pass

    @abstractmethod
    def hide_bonus(self):
        pass


class HealBonus():
    BONUS_HP = 1
    BONUS_SCORE = 50
    image = load_image("cat.png")

    def __init__(self, pos, size):
        self.hp = HealBonus.BONUS_HP
        self.score = HealBonus.BONUS_SCORE
        self.view = DrawWithSprite(pos, size, HealBonus.image)

    def is_collected(self):
        pass

    def add_bonus(self):
        pass

    def hide_bonus(self):
        pass

    def heal_player(self):
        pass


class SimpleBonus(BaseBonus):
    BONUS_SCORE = 50
