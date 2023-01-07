import sys

import pygame
from pygame_gui import UIManager
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIWindow, UIButton

import game_mode
from cringario_util import load_image, terminate
from drawable import *
from level_init import Level
from levels.test_level import *
from player import Hero

import pygame_gui

pygame.init()

screen_width = 1200
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

border = 50

manager = pygame_gui.UIManager(
    (screen_width + 2 * border, screen_height + 2 * border), 'single_play_button.json'
)
window = UIWindow(
    rect=pygame.Rect(
        (-border, -border),
        (screen_width + 2 * border, screen_height + 2 * border)),
    manager=manager,
)

test_image = load_image('main_menu.jpg')

single_play_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 390), (130, 50)),
    text='single play',
    manager=manager,
    container=window,
)
competitive_play_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 460), (130, 50)),
    text='competitive',
    manager=manager,
    container=window,
)
window.image = test_image
single_play_button.get_relative_rect()
competitive_play_button.get_relative_rect()


# image = pygame.transform.scale(test_image, (100, 50))
# switch.image = image
# switch.rect = image.get_rect()
# switch.rect.topleft = (350, 300)


class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.solo_game = game_mode.SingleplayerGameMode(self.screen)
        self.competitive_game = game_mode.MultiplayerGameMode(self.screen)

    def _game_cycle(self):
        running = True
        while running:
            time_delta = timer.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == single_play_button:
                            window.hide()
                            self.start('solo')
                        if event.ui_element == competitive_play_button:
                            window.hide()
                            self.start('competitive')
                manager.process_events(event)

            # self.screen.fill('#123456')
            manager.update(time_delta)
            manager.draw_ui(self.screen)
            pygame.display.flip()

    def start(self, mode):
        if mode == 'solo':
            self.solo_game.run()
        if mode == 'competitive':
            self.competitive_game.run()

    def run(self):
        self._game_cycle()


def main():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    game_manager = GameManager(screen)
    game_manager.run()
    pygame.quit()


if __name__ == '__main__':
    main()
