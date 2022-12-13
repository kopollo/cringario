import pygame

from cringario_util import load_image
from drawable import DrawWithSprite
from tiles import Tile
from levels.test_level import platform_size


class Level:
    def __init__(self, level_map, surface):
        self.display = surface
        self.platforms = pygame.sprite.Group()
        self.setup_level(level_map)
        d = DrawWithSprite((0, 0), 800, load_image("forest.png"))
        self.fon = pygame.sprite.Group(d)

    def setup_level(self, level_map):
        for row_idx, row in enumerate(level_map):
            for col_idx, cell in enumerate(row):
                if cell == '-':
                    x = col_idx * platform_size
                    y = row_idx * platform_size
                    platform = Tile((x, y), platform_size)
                    self.platforms.add(platform.view)

    def run(self):
        self.fon.draw(self.display)
        self.platforms.draw(self.display)



