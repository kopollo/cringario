"""Contain game manager."""
import pygame
import pygame_gui

from cringario_util import terminate

from config_parser import timer
from game_mode import SingleplayerGameMode, MultiplayerGameMode
from windows_manager import (
    gui_manager, window_manager,
)


class GameManager:
    """Class controls game mode initialization, game cycle, windows."""

    def __init__(self, screen):
        """
        Initialize main display.

        :param screen: screen where game is going.
        """
        self.screen = screen
        self.level_map = None
        self.game = None
        self.game_mode = None
        self.is_game_started = False

        self.esc_count = 0

    def _game_cycle(self):
        """Run game cycle.Draw gui, level."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        self.esc_count += 1

                self.check_buttons(event)
                gui_manager.process_events(event)
            self.screen.fill('#123456')
            if self.esc_count % 2 == 1:
                self.game.is_freeze = True
                window_manager.pause_game()
            else:
                if self.game is not None:
                    self.game.is_freeze = False
                    window_manager.pause_window.hide()

            #     window_manager.pause_window.show()
            self.run_game()
            self.draw_gui()
            # if not window_manager.pause_window.visible:
            # self.is_game_started = True

            pygame.display.flip()

    def draw_gui(self):
        """Draw gui by gui_manager."""
        time_delta = timer.tick(60) / 1000
        gui_manager.update(time_delta)
        gui_manager.draw_ui(self.screen)

    def create_game(self):
        """Create a game mode depending on the pressed key."""
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

    def check_buttons(self, event):
        """Check pressed buttons and run their logic."""
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if (event.ui_element ==
                        window_manager.pause_window.cancel_button):
                    window_manager.pause_window.kill()
                    self.esc_count += 1
                if (event.ui_element ==
                        window_manager.pause_window.confirm_button):
                    self.esc_count += 1
                    self.__init__(self.screen)
                    window_manager.start_window.show()
                if (event.ui_element ==
                        window_manager.pause_window.close_window_button):
                    window_manager.pause_window.kill()
                    self.esc_count += 1
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

    def run_game(self):
        """Control game existence."""
        if self.is_game_started:
            if not self.game:
                self.create_game()
            self.game.draw()
            if self.game.is_game_over():
                self.game = None
                self.is_game_started = False
                window_manager.score_window.show()

    def run(self):
        """Run game cycle."""
        self._game_cycle()
