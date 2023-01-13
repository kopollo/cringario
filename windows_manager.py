import pygame
import pygame_gui
from pygame_gui.elements import UIWindow, UIButton

from cringario_util import load_image, terminate, read_config

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

start_window = UIWindow(
    rect=pygame.Rect(*window_rect_coords),
    manager=gui_manager,
)

single_play_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 390), button_size),
    text='single play',
    manager=gui_manager,
    container=start_window,
)
competitive_play_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 460), button_size),
    text='competitive',
    manager=gui_manager,
    container=start_window,
)
start_menu_image = load_image('main_menu.jpg')
start_window.image = start_menu_image

score_window = UIWindow(
    rect=pygame.Rect(*window_rect_coords),
    manager=gui_manager,
    visible=False,
)
score_window_image = load_image('score.png')
score_window.image = score_window_image

back_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((window_width // 2 - border, 660), button_size),
    text='to main menu',
    manager=gui_manager,
    container=score_window,
)
label_width, label_height = label_size
first_player_result_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((center - label_width, 260), label_size),
    text='',
    manager=gui_manager,
    container=score_window,
)
second_player_result_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((center - label_width, 360), label_size),
    text='',
    manager=gui_manager,
    container=score_window,
)
select_lvl_window = UIWindow(
    rect=pygame.Rect(*window_rect_coords),
    manager=gui_manager,
    visible=False,
)

select_lvl_image = pygame.transform.scale(
    load_image('finish_fon.png'),
    (window_width, window_height),
)
select_lvl_window.image = select_lvl_image

lvl_1_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 460), button_size),
    text='LEVEL 1',
    manager=gui_manager,
    container=select_lvl_window,
)
lvl_2_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((500, 460), button_size),
    text='LEVEL 2',
    manager=gui_manager,
    container=select_lvl_window,
)
lvl_3_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((900, 460), button_size),
    text='LEVEL 3',
    manager=gui_manager,
    container=select_lvl_window,
)

# class WindowManager:
#     def __init__(self, screen):
#         self.screen = screen
#
#     def get_pressed_button(self, event):
#         if event.type == pygame.QUIT:
#             terminate()
#
#                     # return 'competitive'
#
#         gui_manager.process_events(event)
#
#     def draw(self):
#         time_delta = timer.tick(60) / 1000
#         gui_manager.update(time_delta)
#         gui_manager.draw_ui(self.screen)
#         pygame.display.flip()
