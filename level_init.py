import pygame

from cringario_util import load_image
from drawable import DrawWithSprite
from tiles import Tile
from levels.test_level import (
    platform_size, screen_width, screen_height,
    map_height)
from bonuses import HealBonus, SimpleBonus
from player import Hero


class Camera:
    pass


class Level:
    def __init__(self, level_map, surface):
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.display = surface
        self.platforms = pygame.sprite.Group()

        self.bonuses = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.setup_level(level_map)

        fon = DrawWithSprite((0, 0), 2000, load_image('secret.png'))
        self.game_fon = pygame.sprite.GroupSingle(fon)

    def setup_level(self, level_map):
        for row_idx, row in enumerate(level_map):
            for col_idx, cell in enumerate(row):
                x = col_idx * platform_size
                y = row_idx * platform_size + screen_height - map_height
                if cell == '-':
                    platform = Tile((x, y), platform_size)
                    self.platforms.add(platform)
                elif cell == 'h':
                    bonus = HealBonus((x, y), platform_size)
                    self.bonuses.add(bonus)
                elif cell == 's':
                    bonus = SimpleBonus((x, y), platform_size)
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
            self.world_shift_x = 8
            player.rect.x += camera_bound - player_x

        elif player_x > screen_width - camera_bound and direction_x > 0:
            self.world_shift_x = -8
            player.rect.x -= player_x - (screen_width - camera_bound)
        else:
            self.world_shift_x = 0

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.direction.x = 0
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.direction.x = 0

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.gravity_work()
        for sprite in self.platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.in_air = False
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

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

        self.platforms.update(self.world_shift_x)
        self.platforms.draw(self.display)

        self.horizontal_movement_collision()
        self.vertical_movement_collision()

        self.player.draw(self.display)
        self.player.update()
