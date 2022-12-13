import pygame

from cringario_util import load_image
from drawable import DrawWithSprite
from tiles import Tile
from levels.test_level import platform_size
from bonuses import HealBonus
from player import Hero

class Level:
    def __init__(self, level_map, surface):
        self.display = surface
        self.platforms = pygame.sprite.Group()
        self.bonuses = pygame.sprite.Group()

        self.player = pygame.sprite.GroupSingle()

        self.setup_level(level_map)
        d = DrawWithSprite((0, 0), 800, load_image("forest.png"))
        self.fon = pygame.sprite.Group(d)

    def setup_level(self, level_map):
        for row_idx, row in enumerate(level_map):
            for col_idx, cell in enumerate(row):
                x = col_idx * platform_size
                y = row_idx * platform_size
                if cell == '-':
                    platform = Tile((x, y), platform_size)
                    self.platforms.add(platform.view)
                elif cell == 'x':
                    bonus = HealBonus((x, y), platform_size)
                    self.bonuses.add(bonus.view)
                elif cell == 'P':
                    player_sprite = Hero((x, y)).view
                    self.player.add(player_sprite)


    # def scroll_x(self):
    #     player = self.
    def run(self):
        self.fon.draw(self.display)
        self.platforms.draw(self.display)
        self.bonuses.draw(self.display)
        # self.player.draw(self.display)
