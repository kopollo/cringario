import pygame

from level_init import Level
from levels.test_level import level_map
from drawable import *
from cringario_util import load_image
from window_objects.windows import StartWindow
WINDOW_SIZE = 800, 700
timer = pygame.time.Clock()


class GameManager:
    def _draw_frame(self, screen):
        screen.fill('#123456')
        w = StartWindow(screen)
        w.render()
        # level = Level(level_map, screen)
        # level.run()
        pygame.display.flip()
        timer.tick(60)

    def _game_cycle(self, screen):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self._draw_frame(screen)

    def run(self):
        screen = pygame.display.set_mode(WINDOW_SIZE)
        self._game_cycle(screen)


def main():
    pygame.init()
    manager = GameManager()
    manager.run()
    pygame.quit()


if __name__ == '__main__':
    main()
