"""Contain ground class."""
from drawable import DrawWithSprite


class Ground(DrawWithSprite):
    """Ground object on which you can walk."""

    def __init__(self, pos, size, image):
        """
        Initialize ground object.

        :param pos: position for ground object
        :param size: size of ground object
        :param image: sprite for ground object
        """
        super().__init__(pos, size, image)

    def update(self, shift_x):
        """
        Scroll x coordinate ground object.

        :param shift_x: value of shift
        """
        self.rect.x += shift_x
