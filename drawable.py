"""Contain pygame sprite covers."""
import pygame


class BaseSprite(pygame.sprite.Sprite):
    """Simple sprite cover."""

    def __init__(self):
        """Initialize pygame.sprite.Sprite."""
        super().__init__()


class DrawWithColor(BaseSprite):
    """Sprite that looks like filled rectangle."""

    def __init__(self, pos, size, color='grey'):
        """
        Initialize sprite.

        :param pos: left bottom corner
        :param size: size of rect
        :param color: color of rect
        """
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)


class DrawWithSprite(BaseSprite):
    """Sprite that looks like image."""

    def __init__(self, pos, size, image):
        """
        Initialize sprite.

        :param pos: left bottom corner
        :param size: size of rect
        :param image: image of sprite
        """
        super().__init__()
        width, height = size
        image = pygame.transform.scale(image, (width, height))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


class DrawWithText(BaseSprite):
    """Sprite that looks like text."""

    def __init__(self, pos, text):
        """
        Initialize sprite. The size depends on the length of the text.

        :param pos: left bottom corner
        :param text: text of sprite
        """
        super().__init__()
        font = pygame.font.Font(None, 40)
        self.text = font.render(text, True, 'white')
        self.width = self.text.get_width()
        self.height = self.text.get_height()
        self.image = pygame.transform.scale(
            self.text, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.image.blit(
            self.text,
            [self.width / 2 - self.width / 2,
             self.height / 2 - self.height / 2])
