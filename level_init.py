import pygame

from cringario_util import load_image
from drawable import DrawWithSprite
from tiles import Tile
from levels.test_level import platform_size, screen_width
from bonuses import HealBonus
from player import Hero


class Level:
    def __init__(self, level_map, surface):
        self.world_shift = 0
        self.display = surface
        self.platforms = pygame.sprite.Group()

        self.bonuses = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.setup_level(level_map)

        # d = DrawWithSprite((0, 0), 800, load_image("forest.png"))
        # self.fon = pygame.sprite.Group(d)

    def setup_level(self, level_map):
        for row_idx, row in enumerate(level_map):
            for col_idx, cell in enumerate(row):
                x = col_idx * platform_size
                y = row_idx * platform_size
                if cell == '-':
                    platform = Tile((x, y), platform_size)
                    self.platforms.add(platform)
                elif cell == 'x':
                    bonus = HealBonus((x, y), platform_size)
                    self.bonuses.add(bonus)
                elif cell == 'P':
                    player_sprite = Hero((x, y), 40)
                    self.player.add(player_sprite)

    def scroll_x(self):

        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        camera_bound = screen_width / 6
        if player_x < camera_bound and direction_x < 0:
            self.world_shift = 8
            player.speed = 0

        elif player_x > screen_width - camera_bound and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.gravity_work()

        for sprite in self.platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom





    def run(self):
        self.player.update()
        self.bonuses.draw(self.display)
        # self.fon.draw(self.display)
        self.platforms.draw(self.display)
        self.player.draw(self.display)

        self.scroll_x()
        self.platforms.update(self.world_shift)

        self.horizontal_movement_collision()
        self.vertical_movement_collision()
