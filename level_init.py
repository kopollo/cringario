import pygame
from platform import Platform
from levels.test_level import platform_size


class Level:
    def __init__(self, level_map, surface):
        self.display = surface
        self.platforms = pygame.sprite.Group()
        self.setup_level(level_map)

    def setup_level(self, level_map):
        for row_idx, row in enumerate(level_map):
            for col_idx, cell in enumerate(row):
                if cell == '-':
                    x = col_idx * platform_size
                    y = row_idx * platform_size
                    platform = Platform((x, y), platform_size)
                    self.platforms.add(platform)

    def run(self):
        self.platforms.draw(self.display)


