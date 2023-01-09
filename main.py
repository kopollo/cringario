import sys
import pygame
import pygame_gui
import yaml

import levels.lvl_2
from cringario_util import terminate

from config_parser import (
    screen_width, screen_height, timer, platform_size,
    player_size,screen_size
)
from game_mode import SingleplayerGameMode, MultiplayerGameMode
from windows_manager import (
    start_window, single_play_button,
    competitive_play_button, back_button, gui_manager,
)


class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.level_map = levels.lvl_2.level_map
        # self.window_manager = WindowManager(self.screen)
        self.game = None

    def _game_cycle(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == single_play_button:
                            start_window.hide()
                            self.game = SingleplayerGameMode(
                                self.screen,
                                self.level_map,
                            )
                        if event.ui_element == competitive_play_button:
                            start_window.hide()
                            self.game = MultiplayerGameMode(
                                self.screen,
                                self.level_map,
                            )
                        if event.ui_element == back_button:
                            start_window.show()
                gui_manager.process_events(event)
            self.screen.fill('#123456')
            if self.game is not None:
                self.game.draw()
                if self.game.is_game_over():
                    self.game = None
                    start_window.show()
            self.draw_gui()

            pygame.display.flip()

    def draw_gui(self):
        time_delta = timer.tick(60) / 1000
        gui_manager.update(time_delta)
        gui_manager.draw_ui(self.screen)

    def run(self):
        self._game_cycle()


def main():
    screen = pygame.display.set_mode(screen_size)
    game_manager = GameManager(screen)
    game_manager.run()
    pygame.quit()


if __name__ == '__main__':
    main()
