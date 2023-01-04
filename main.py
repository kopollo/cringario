import pygame

from drawable import *
from level_init import Level
from levels.test_level import *

from cringario_util import load_image
from player import Hero
from window_objects.windows import StartWindow

screen_width = 1024
screen_height = 800

WINDOW_SIZE = screen_width, screen_height
timer = pygame.time.Clock()

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


def create_level(surface, player_sprite, k):
    level = Level(
        level_map,
        surface,
        platform_size // k,
        screen_width,
        screen_height // k,
        map_height // k,
        player_sprite
    )
    return level


class MultiplayerGameManager:
    def __init__(self, screen):
        self.screen = screen

        self.first_player_game_field = pygame.Surface((screen_width,
                                                       screen_height // 2))
        self.second_player_game_field = pygame.Surface((screen_width,
                                                        screen_height // 2))

    def _game_cycle(self, screen):
        running = True

        first_player_hero = Hero((0, 0), (20, 20), controller1)
        level1 = create_level(self.first_player_game_field,
                              first_player_hero, 2)

        second_player_hero = Hero((0, 0), (20, 20), controller2)
        level2 = create_level(self.second_player_game_field,
                              second_player_hero, 2)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill('#123456')
            screen.blit(self.first_player_game_field, (0, 0))
            screen.blit(self.second_player_game_field, (0, screen_height // 2))
            level1.run()
            level2.run()
            pygame.display.flip()
            timer.tick(60)

    def run(self):
        self._game_cycle(self.screen)


class SingleplayerGameManager:
    def __init__(self, screen):
        self.screen = screen

        self._game_field = pygame.Surface((screen_width,
                                           screen_height))

    def _game_cycle(self, screen):
        running = True

        player_hero = Hero((0, 0), (40, 40), controller1)
        level = create_level(self._game_field,
                             player_hero, 1)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill('#123456')
            screen.blit(self._game_field, (0, 0))
            level.run()
            pygame.display.flip()
            timer.tick(60)

    def run(self):
        self._game_cycle(self.screen)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    manager = SingleplayerGameManager(screen)
    manager.run()
    pygame.quit()


if __name__ == '__main__':
    main()
