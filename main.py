import pygame
import pygame_gui

from levels import (
    lvl_1, lvl_2, lvl_3
)
from cringario_util import terminate

from config_parser import timer, screen_size
from game_mode import SingleplayerGameMode, MultiplayerGameMode
from windows_manager import (
    # back_button, , score_window,
    gui_manager, window_manager,
    # select_lvl_window, StartWindow,
    # lvl_1_button, lvl_2_button, lvl_3_button,
)


class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.level_map = lvl_2.level_map
        # self.window_manager = WindowManager(self.screen)
        self.game = None
        self.game_mode = None
        self.is_game_started = False

        # self.start_window = StartWindow()

    def _game_cycle(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if (event.ui_element ==
                                window_manager.start_window.single_play_button):
                            window_manager.start_window.hide()
                            window_manager.level_select_window.show()
                            self.game_mode = 'singleplayer'
                        if (event.ui_element ==
                                window_manager.start_window.competitive_play_button):
                            window_manager.start_window.hide()
                            window_manager.level_select_window.show()
                            self.game_mode = 'multiplayer'
                        if (event.ui_element ==
                                window_manager.score_window.back_button):
                            window_manager.score_window.hide()
                            window_manager.start_window.show()
                        for level in window_manager.level_select_window.level_buttons:
                            if event.ui_element == level:
                                self.level_map = level.level_map
                                window_manager.level_select_window.hide()
                                self.is_game_started = True

                gui_manager.process_events(event)
            self.screen.fill('#123456')
            self.draw_gui()
            if self.is_game_started:
                if not self.game:
                    self.create_game()
                self.game.draw()
                if self.game.is_game_over():
                    self.game = None
                    self.is_game_started = False
                    window_manager.score_window.show()
            pygame.display.flip()

    def draw_gui(self):
        time_delta = timer.tick(60) / 1000
        gui_manager.update(time_delta)
        gui_manager.draw_ui(self.screen)

    def create_game(self):
        if self.game_mode == 'singleplayer':
            self.game = SingleplayerGameMode(
                self.screen,
                self.level_map,
            )
        elif self.game_mode == 'multiplayer':
            self.game = MultiplayerGameMode(
                self.screen,
                self.level_map,
            )

    def run(self):
        self._game_cycle()


def main():
    screen = pygame.display.set_mode(screen_size)
    game_manager = GameManager(screen)
    game_manager.run()
    pygame.quit()


if __name__ == '__main__':
    main()
