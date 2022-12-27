import pygame

from drawable import *
from level_init import Level
from levels.test_level import level_map, screen_width, screen_height
from cringario_util import load_image
from window_objects.windows import StartWindow

WINDOW_SIZE = screen_width, screen_height
timer = pygame.time.Clock()


class GameManager:
    def __init__(self, screen):
        self.screen = screen

    def _game_cycle(self, screen):
        running = True
        level = Level(level_map, screen)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill('#123456')
            level.run()
            pygame.display.flip()
            timer.tick(60)

    def run(self):
        self._game_cycle(self.screen)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    manager = GameManager(screen)
    manager.run()
    pygame.quit()


if __name__ == '__main__':
    main()
