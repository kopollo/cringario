import pygame


class DrawWithColor(pygame.sprite.Sprite):
    def __init__(self, pos, size, color='grey'):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)


class DrawWithSprite(pygame.sprite.Sprite):
    def __init__(self, pos, size, image):
        super().__init__()
        width, height = size
        image = pygame.transform.scale(image, (width, height))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


class DrawWithText(pygame.sprite.Sprite):
    def __init__(self, pos, text):
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
