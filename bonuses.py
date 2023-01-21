"""Contain BaseBonus and its implementations."""
from abc import ABC, abstractmethod

from drawable import DrawWithSprite


class BaseBonus(ABC, DrawWithSprite):
    """Abstract class that must be implemented by every bonus."""

    @abstractmethod
    def add_bonus(self, player):
        """
        Add bonus to player.

        :param player: the player that catch bonus
        """
        pass

    def hide_bonus(self):
        """Hide bonus."""
        self.kill()

    def update(self, shift_x):
        """
        Update sprite coordinates.

        :param shift_x: shift of scroll
        """
        self.rect.x += shift_x


class HealBonus(BaseBonus, DrawWithSprite):
    """Bonus can add score and heal points."""

    BONUS_HP = 1
    BONUS_SCORE = 50

    def __init__(self, pos, size, image):
        """
        Initialize of bonus.

        :param pos: left bottom corner
        :param size: size of bonus (width, height)
        :param image: image
        """
        super().__init__(pos, size, image)
        self.hp = HealBonus.BONUS_HP
        self.score = HealBonus.BONUS_SCORE

    def add_bonus(self, player):
        """
        Add bonus to player.

        :param player: the player that catch bonus
        """
        player.add_score(self.score)
        player.add_hp(self.hp)


class SimpleBonus(BaseBonus, DrawWithSprite):
    """Bonus that add only score."""

    BONUS_SCORE = 100

    def __init__(self, pos, size, image):
        """
        Initialize of bonus.

        :param pos: left bottom corner
        :param size: size of bonus (width, height)
        :param image: image
        """
        super().__init__(pos, size, image)
        self.score = SimpleBonus.BONUS_SCORE

    def add_bonus(self, player):
        """
        Add bonus to player.

        :param player: the player that catch bonus
        """
        player.add_score(self.score)
