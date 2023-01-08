from abc import ABC, abstractmethod

import pygame

# from drawable import *
from level_init import Level
# from levels.test_level import *
from player import Hero
from game_parameters import screen_width, screen_height, timer, platform_size, \
    player_size
from cringario_util import terminate

controller1 = {
    'left': pygame.K_a,
    'right': pygame.K_d,
    'up': pygame.K_w,
}
controller2 = {
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'up': pygame.K_UP,
}


class BaseGameMode(ABC):
    @abstractmethod
    def draw(self):
        pass

    def _game_cycle(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
            self.draw()
            timer.tick(60)

    def run(self):
        self._game_cycle()


def create_level(surface, player_sprite, level_map, k):
    level = Level(
        level_map,
        surface,
        platform_size,
        screen_width,
        screen_height // k,
        player_sprite,
    )
    return level


class SingleplayerGameMode(BaseGameMode):
    def __init__(self, screen, level_map):
        super().__init__()
        self.screen = screen
        self.time_delta = 0
        self.level_map = level_map
        self._game_field = pygame.Surface(
            (screen_width, screen_height)
        )

        self.player_hero = Hero((0, 0), player_size, controller1)
        self.level = create_level(
            self._game_field,
            self.player_hero,
            self.level_map,
            k=1)

    def draw(self):
        self.screen.fill('#123456')
        self.screen.blit(self._game_field, (0, 0))
        self.level.run()
        pygame.display.flip()


class MultiplayerGameMode(BaseGameMode):
    def __init__(self, screen, level_map):
        self.screen = screen
        self.level_map = level_map

        self.first_player_game_field = pygame.Surface(
            (screen_width,
             screen_height // 2))
        self.second_player_game_field = pygame.Surface(
            (screen_width,
             screen_height // 2))

        self.first_player_hero = Hero((0, 0), player_size, controller1)
        self.level1 = create_level(
            self.first_player_game_field,
            self.first_player_hero,
            self.level_map,
            k=2)

        self.second_player_hero = Hero((0, 0), player_size, controller2)
        self.level2 = create_level(
            self.second_player_game_field,
            self.second_player_hero,
            self.level_map,
            k=2)

    def draw(self):
        self.screen.fill('#123456')
        self.screen.blit(self.first_player_game_field, (0, 0))
        self.screen.blit(self.second_player_game_field, (0, screen_height // 2))
        self.level1.run()
        self.level2.run()
        pygame.display.flip()
