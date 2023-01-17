"""Contains PlayerStateIndicator."""
from drawable import DrawWithText
import pygame


class PlayerStateIndicator:
    """Draw user info: hp, score, time."""

    def __init__(self, width, height, player, display):
        """
        Initialize PlayerStateIndicator.

        :param width: width of indicator
        :param height: height of indicator
        :param player: player from whom we get info
        :param display: display where we show info
        """
        self.display = display
        self.player = player
        self.width = width
        self.height = height
        self.sprite_group = pygame.sprite.Group()
        self.start_ticks = pygame.time.get_ticks()
        self.seconds = 0

    def run(self):
        """Draw player info."""
        self._update_info()
        self.sprite_group.draw(self.display)

    def _update_info(self):
        """Update info which we wanted to show."""
        self.seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000
        data = [
            f'HP : {self.player.hp}',
            f'SCORE : {self.player.score}',
            f'TIME : {self.seconds}',
        ]
        self.sprite_group = pygame.sprite.Group()
        for i, val in enumerate(data):
            self.sprite_group.add(DrawWithText(
                (self.width, self.height + 50 * i), val))
