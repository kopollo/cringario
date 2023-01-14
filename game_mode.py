"""Contain game modes classes"""
from abc import ABC, abstractmethod

import pygame

from level_init import Level
from player import Hero
from config_parser import (
    screen_width, screen_height, platform_size,
    player_size,
)
from windows_manager import (
    window_manager,
)

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

    @abstractmethod
    def is_game_over(self):
        pass

    def create_level(self, surface, player_sprite, level_map, height_coef):
        level = Level(
            level_map,
            surface,
            platform_size,
            screen_width,
            screen_height // height_coef,
            player_sprite,
        )
        return level

    @abstractmethod
    def set_result_view(self):
        pass


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
        self.level = self.create_level(
            self._game_field,
            self.player_hero,
            self.level_map,
            height_coef=1)

    def draw(self):
        self.screen.blit(self._game_field, (0, 0))
        self.level.run()
        pygame.display.flip()

    def is_game_over(self):
        if self.level.check_is_game_over():
            self.set_result_view()
            return True

    def set_result_view(self):
        window_manager.score_window.first_player_result_label.set_text(
            f"FIRST PLAYER SCORE: {self.player_hero.score}\n"
        )


class MultiplayerGameMode(BaseGameMode):
    def __init__(self, screen, level_map):
        self.screen = screen
        self.level_map = level_map
        self.is_over = False

        self.first_player_game_field = pygame.Surface(
            (screen_width,
             screen_height // 2))
        self.second_player_game_field = pygame.Surface(
            (screen_width,
             screen_height // 2))

        self.first_player_hero = Hero((0, 0), player_size, controller1)
        self.level1 = self.create_level(
            self.first_player_game_field,
            self.first_player_hero,
            self.level_map,
            height_coef=2)

        self.second_player_hero = Hero((0, 0), player_size, controller2)
        self.level2 = self.create_level(
            self.second_player_game_field,
            self.second_player_hero,
            self.level_map,
            height_coef=2)

    def draw(self):
        self.screen.blit(self.first_player_game_field, (0, 0))
        self.screen.blit(self.second_player_game_field, (0, screen_height // 2))
        self.draw_level(self.level1)
        self.draw_level(self.level2)
        pygame.display.flip()

    def draw_level(self, level):
        if not level.check_is_game_over():
            level.run()

    def is_game_over(self):
        if (self.level1.check_is_game_over() and
                self.level2.check_is_game_over()):
            self.set_result_view()
            return True

    def set_result_view(self):
        window_manager.score_window.first_player_result_label.set_text(
            f"FIRST PLAYER SCORE: {self.first_player_hero.score}\n"
        )
        window_manager.score_window.second_player_result_label.set_text(
            f"FIRST PLAYER SCORE: {self.second_player_hero.score}\n"
        )
        # second_player_result_label.set_text("uuuu")
