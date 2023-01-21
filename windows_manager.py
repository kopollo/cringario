"""Contain window classes and their manager."""
import pygame
import pygame_gui  # type: ignore
from pygame_gui.elements import UIWindow, UIButton  # type: ignore
from pygame_gui.windows import UIConfirmationDialog  # type: ignore

from cringario_util import load_image, read_config, load_level

from config_parser import (
    screen_width, screen_height,
)

config = read_config()["window_elements"]

button_size = config["button_size"]
border = config["border"]
label_size = config["label_size"]

window_height = screen_height + 2 * border
window_width = screen_width + 2 * border
center = window_width // 2
window_rect_coords = (-border, -border), (window_width, window_height)
gui_manager = pygame_gui.UIManager(
    (window_width, window_height),
    'theme.json'
)


class StartWindow(UIWindow):
    """Start window with game mode chooser."""

    def __init__(self):
        """Initialize buttons in window."""
        super().__init__(
            rect=pygame.Rect(*window_rect_coords),
            manager=gui_manager,
        )
        self.single_play_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 390), button_size),
            text='single play',
            manager=gui_manager,
            container=self,
        )
        self.competitive_play_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 460), button_size),
            text='competitive',
            manager=gui_manager,
            container=self,
        )
        start_menu_image = load_image('main_menu.jpg')
        self.image = start_menu_image


class ScoreWindow(UIWindow):
    """Window show player score after game."""

    def __init__(self):
        """Initialize buttons in window."""
        super().__init__(
            rect=pygame.Rect(*window_rect_coords),
            manager=gui_manager,
            visible=False,
        )

        self.back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (window_width // 2 - border, 660), button_size),
            text='to main menu',
            manager=gui_manager,
            container=self,
        )
        label_width, label_height = label_size
        self.first_player_result_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((center - label_width, 260), label_size),
            text='',
            manager=gui_manager,
            container=self,
        )
        self.second_player_result_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((center - label_width, 360), label_size),
            text='',
            manager=gui_manager,
            container=self,
        )
        score_window_image = pygame.transform.scale(
            load_image('wow.png'),
            (window_width, window_height),
        )
        self.image = score_window_image


class LevelSelectWindow(UIWindow):
    """Window with list of buttons to select level."""

    def __init__(self):
        """Initialize buttons in window."""
        super().__init__(
            rect=pygame.Rect(*window_rect_coords),
            manager=gui_manager,
            visible=False,
        )

        select_lvl_image = pygame.transform.scale(
            load_image('sfon.png'),
            (window_width, window_height),
        )
        self.image = select_lvl_image
        all_lvl = ["lvl_1.txt", "lvl_2.txt", "lvl_3.txt"]
        self.level_buttons = []
        for i in range(3):
            btn = LevelSelectButton(
                rect=pygame.Rect((100 + 400 * i, 460), button_size),
                container=self,
                text=f"level {i + 1}",
                level_map=load_level(all_lvl[i])
            )
            self.level_buttons.append(btn)


class PauseWindow(UIConfirmationDialog):
    """Window with list of buttons to select level."""

    def __init__(self):
        """Initialize buttons in window."""
        super().__init__(
            action_long_desc="ARE YOU REALLY WANT TO EXIT?",
            rect=pygame.Rect((200, 100), (500, 300)),
            manager=gui_manager,
            visible=False,
        )


class LevelSelectButton(UIButton):
    """Button for LevelSelectWindow that contain level map."""

    def __init__(self, container, rect, text, level_map):
        """Initialize button."""
        super().__init__(
            relative_rect=rect,
            text=text,
            manager=gui_manager,
            container=container,
        )
        self.level_map = level_map


class WindowManager:
    """Unite all windows in one place."""

    def __init__(self):
        """Initialize windows."""
        self.start_window = StartWindow()
        self.score_window = ScoreWindow()
        self.level_select_window = LevelSelectWindow()
        self.pause_window = PauseWindow()

    def pause_game(self):
        """Show pause window."""
        if not self.pause_window.visible:
            self.pause_window = PauseWindow()
        self.pause_window.show()

    def unpause_game(self):
        """Hide pause window."""
        self.pause_window.hide()


window_manager = WindowManager()
