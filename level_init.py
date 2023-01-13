import pygame

from collision import Collision
from drawable import DrawWithSprite
from enemy import Enemy
from ground import Ground
from bonuses import HealBonus, SimpleBonus
from player_state_indicator import PlayerStateIndicator
from game_over_object import WinObject

from config_parser import (
    heal_bonus_image, simple_bonus_image, game_fon,
    platform_image, enemy_image, win_cup_image, grass_image, dirt_image
)


class Level:
    def __init__(self, level_map, surface,
                 platform_size, screen_width,
                 screen_height, player):
        self.world_shift_x = 0
        self.total_shift_x = 0
        self.display = surface
        self.platforms = pygame.sprite.Group()
        self.ground = pygame.sprite.Group()
        self.player = player

        self.platform_size = platform_size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_height = platform_size * len(level_map)

        self.bonuses = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.cup_sprite = pygame.sprite.GroupSingle()
        self.player_sprite = pygame.sprite.GroupSingle()
        self.player_state_indicator = PlayerStateIndicator(
            self.screen_width - 250, 20,
            self.player, self.display,
        )
        self.setup_level(level_map)

        fon = DrawWithSprite(
            (0, 0),
            (screen_width, screen_height), game_fon
        )
        self.game_fon = pygame.sprite.GroupSingle(fon)

        self.player_collision = Collision(self.player_sprite, self.platforms)
        self.enemy_collision = Collision(self.enemies, self.platforms)

    def setup_level(self, level_map):
        platform_size = self.platform_size
        for row_idx, row in enumerate(level_map):
            for col_idx, cell in enumerate(row):
                x = col_idx * platform_size
                y = (row_idx * platform_size +
                     self.screen_height - self.map_height)
                if cell == '-':
                    platform = Ground(
                        (x, y), (platform_size, platform_size),
                        platform_image,
                    )
                    self.platforms.add(platform)
                elif cell == 'g':
                    ground = Ground(
                        (x, y), (platform_size, platform_size),
                        grass_image,
                    )
                    self.platforms.add(ground)
                elif cell == 'd':
                    ground = Ground(
                        (x, y), (platform_size, platform_size),
                        dirt_image,
                    )
                    self.platforms.add(ground)
                elif cell == 'h':
                    bonus = HealBonus(
                        (x, y), (platform_size, platform_size),
                        heal_bonus_image,
                    )
                    self.bonuses.add(bonus)
                elif cell == 's':
                    bonus = SimpleBonus(
                        (x, y), (platform_size, platform_size),
                        simple_bonus_image,
                    )
                    self.bonuses.add(bonus)
                elif cell == 'w':
                    cup = WinObject(
                        (x, y), (platform_size, platform_size),
                        win_cup_image)
                    self.cup_sprite.add(cup)
                elif cell == 'e':
                    enemy = Enemy(
                        (x, y), (platform_size, platform_size),
                        enemy_image)
                    self.enemies.add(enemy)
                elif cell == 'P':
                    self.player.relocate_to((x, y))
                    self.player.spawn_point = (x, y)
                    self.player_sprite.add(self.player)

    def scroll_x(self):
        world_shift_speed = 8
        player = self.player
        player_x = player.rect.centerx
        direction_x = player.direction.x
        screen_width = self.screen_width
        camera_bound = screen_width / 4
        if player_x < camera_bound and direction_x < 0:
            self.world_shift_x = world_shift_speed
            player.rect.x += camera_bound - player_x
            self.total_shift_x += world_shift_speed

        elif player_x > screen_width - camera_bound and direction_x > 0:
            self.world_shift_x = -world_shift_speed
            player.rect.x -= player_x - (screen_width - camera_bound)
            self.total_shift_x -= world_shift_speed
        else:
            self.world_shift_x = 0

    def check_bonuses_collision(self):
        player = self.player
        for bonus in self.bonuses:
            if bonus.rect.colliderect(player.rect):
                bonus.hide_bonus()
                bonus.add_bonus(player)

    def check_enemies_collision(self):
        player = self.player
        for enemy in self.enemies:
            if enemy.rect.colliderect(player.rect):
                player.get_damaged(enemy)

    def check_player_state(self):
        player = self.player
        if player.is_dead() or player.rect.centery > self.screen_height:
            player.hp = player.HERO_HEALTH
            player.relocate_to(player.spawn_point)
            self.world_shift_x -= self.total_shift_x
            self.total_shift_x = 0

    def check_is_game_over(self):
        player = self.player
        cup = self.cup_sprite.sprite
        if cup.rect.colliderect(player.rect):
            return True

    def run(self):
        self.scroll_x()

        self.game_fon.draw(self.display)

        self.check_player_state()
        self.check_bonuses_collision()
        self.check_enemies_collision()

        self.bonuses.draw(self.display)
        self.bonuses.update(self.world_shift_x)

        self.cup_sprite.draw(self.display)
        self.cup_sprite.update(self.world_shift_x)

        self.enemies.draw(self.display)
        self.enemies.update(self.world_shift_x)

        self.platforms.update(self.world_shift_x)
        self.platforms.draw(self.display)

        self.ground.update(self.world_shift_x)
        self.ground.draw(self.display)

        self.player_collision.apply()
        self.enemy_collision.apply()

        self.player_sprite.draw(self.display)
        self.player_sprite.update()

        self.player_state_indicator.run()
