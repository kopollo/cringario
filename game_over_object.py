"""Contain win object."""
from drawable import DrawWithSprite


class WinObject(DrawWithSprite):
    """Win object. If it is taken then game over."""

    def __init__(self, pos, size, image):
        """
        Initialize win object.

        :param pos: position for win object
        :param size: size of win object
        :param image: sprite for win object
        """
        super().__init__(pos, size, image)

    def update(self, shift_x):
        """
        Scroll x coordinate ground object.

        :param shift_x: value of shift
        """
        self.rect.x += shift_x
