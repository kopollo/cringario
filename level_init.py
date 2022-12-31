import pygame

from collision import Collision
from cringario_util import load_image
from drawable import DrawWithSprite
from tiles import Tile
from levels.test_level import (
    platform_size, screen_width, screen_height,
    map_height)
from bonuses import HealBonus, SimpleBonus
from moving_objects import Hero, Enemy


class Camera:
    pass


class Level:
    def __init__(self, level_map, surface):
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.display = surface
        self.platforms = pygame.sprite.Group()

        self.bonuses = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.setup_level(level_map)

        fon = DrawWithSprite(
            (0, 0),
            (screen_width, screen_height),
            load_image('mount.png')
        )
        self.game_fon = pygame.sprite.GroupSingle(fon)

        self.player_collision = Collision(self.player, self.platforms)
        self.enemy_collision = Collision(self.enemies, self.platforms)

    def setup_level(self, level_map):
        for row_idx, row in enumerate(level_map):
            for col_idx, cell in enumerate(row):
                x = col_idx * platform_size
                y = row_idx * platform_size + screen_height - map_height
                if cell == '-':
                    platform = Tile((x, y), (platform_size, platform_size))
                    self.platforms.add(platform)
                elif cell == 'h':
                    bonus = HealBonus((x, y), (platform_size, platform_size))
                    self.bonuses.add(bonus)
                elif cell == 's':
                    bonus = SimpleBonus((x, y), (platform_size, platform_size))
                    self.bonuses.add(bonus)
                elif cell == 'e':
                    enemy = Enemy((x, y), (platform_size, platform_size))
                    self.enemies.add(enemy)
                elif cell == 'P':
                    player_sprite = Hero((x, y), (40, 40))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        camera_bound = screen_width / 6
        if player_x < camera_bound and direction_x < 0:
            self.world_shift_x = 8
            player.rect.x += camera_bound - player_x

        elif player_x > screen_width - camera_bound and direction_x > 0:
            self.world_shift_x = -8
            player.rect.x -= player_x - (screen_width - camera_bound)
        else:
            self.world_shift_x = 0

    def check_bonuses(self):
        player = self.player.sprite
        for bonus in self.bonuses:
            if bonus.rect.colliderect(player.rect):
                bonus.hide_bonus()
                bonus.add_bonus(player)

    def check_bonuses(self):
        player = self.player.sprite
        for bonus in self.bonuses:
            if bonus.rect.colliderect(player.rect):
                bonus.hide_bonus()
                bonus.add_bonus(player)

    def run(self):
        self.game_fon.draw(self.display)

        self.scroll_x()

        self.check_bonuses()

        self.bonuses.draw(self.display)
        self.bonuses.update(self.world_shift_x)

        self.enemies.draw(self.display)
        self.enemies.update(self.world_shift_x)

        self.platforms.update(self.world_shift_x)
        self.platforms.draw(self.display)

        self.player_collision.apply()
        self.enemy_collision.apply()

        self.player.draw(self.display)
        self.player.update()
