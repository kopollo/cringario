import pygame
import pygame_gui
from pygame_gui.elements import UIWindow, UIButton

from cringario_util import load_image, read_config

from config_parser import (
    screen_width, screen_height,
)

from levels import (
    lvl_1, lvl_2, lvl_3
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
    def __init__(self):
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
    def __init__(self):
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
            load_image('score_fon2.png'),
            (window_width, window_height),
        )
        self.image = score_window_image


class LevelSelectWindow(UIWindow):
    def __init__(self):
        super().__init__(
            rect=pygame.Rect(*window_rect_coords),
            manager=gui_manager,
            visible=False,
        )

        select_lvl_image = pygame.transform.scale(
            load_image('finish_fon.png'),
            (window_width, window_height),
        )
        self.image = select_lvl_image
        self.lvl_1_button = LevelSelectButton(
            rect=pygame.Rect((100, 460), button_size),
            container=self,
            text="level 1",
            level_map=lvl_1.level_map
        )
        self.lvl_2_button = LevelSelectButton(
            rect=pygame.Rect((500, 460), button_size),
            container=self,
            text="level 2",
            level_map=lvl_2.level_map
        )
        self.lvl_3_button = LevelSelectButton(
            rect=pygame.Rect((900, 460), button_size),
            container=self,
            text="level 3",
            level_map=lvl_3.level_map
        )
        self.level_buttons = [self.lvl_1_button, self.lvl_2_button,
                              self.lvl_3_button]


class LevelSelectButton(UIButton):
    def __init__(self, container, rect, text, level_map):
        super().__init__(
            relative_rect=rect,
            text=text,
            manager=gui_manager,
            container=container,
        )
        self.level_map = level_map


class WindowManager:
    def __init__(self):
        self.start_window = StartWindow()
        self.score_window = ScoreWindow()
        self.level_select_window = LevelSelectWindow()

    # def btn_pressed_checker(self, event):
    #     pass


window_manager = WindowManager()
# def get_pressed_button(self, event):
#     if event.type == pygame.QUIT:
#         terminate()
#
#         # return 'competitive'
#
#     gui_manager.process_events(event)

# def draw(self):
#     time_delta = timer.tick(60) / 1000
#     gui_manager.update(time_delta)
#     gui_manager.draw_ui(self.screen)
#     pygame.display.flip()
