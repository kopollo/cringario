import sys
import pygame
import pygame_gui

# from cringario_util import load_image, terminate
# from game_parameters import *

from game_mode import SingleplayerGameMode, MultiplayerGameMode
from windows_manager import *


class GameManager:
    def __init__(self, screen):
        self.screen = screen
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
                            self.game = SingleplayerGameMode(self.screen)
                        if event.ui_element == competitive_play_button:
                            start_window.hide()
                            self.game = MultiplayerGameMode(self.screen)
                        if event.ui_element == back_button:
                            start_window.show()
                gui_manager.process_events(event)

                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     score_window.show()
            self.draw_gui()
            if self.game is not None:
                self.game.run()
            pygame.display.flip()

    def draw_gui(self):
        time_delta = timer.tick(60) / 1000
        gui_manager.update(time_delta)
        gui_manager.draw_ui(self.screen)

    def run(self):
        self._game_cycle()


def main():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    game_manager = GameManager(screen)
    game_manager.run()
    pygame.quit()


if __name__ == '__main__':
    main()
