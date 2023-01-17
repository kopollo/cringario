"""Entrance point of the program."""
import pygame

from config_parser import screen_size
from game_manager import GameManager


def main():
    """Run program."""
    screen = pygame.display.set_mode(screen_size)
    game_manager = GameManager(screen)
    game_manager.run()
    pygame.quit()


if __name__ == '__main__':
    main()
