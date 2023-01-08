import pygame_gui
from pygame_gui.elements import UIWindow, UIButton

from cringario_util import load_image, terminate
from game_parameters import *

border = 50
gui_manager = pygame_gui.UIManager(
    (screen_width + 2 * border, screen_height + 2 * border),
    'theme.json'
)
start_window = UIWindow(
    rect=pygame.Rect(
        (-border, -border),
        (screen_width + 2 * border, screen_height + 2 * border)),
    manager=gui_manager,
)

single_play_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 390), (130, 50)),
    text='single play',
    manager=gui_manager,
    container=start_window,
)
competitive_play_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 460), (130, 50)),
    text='competitive',
    manager=gui_manager,
    container=start_window,
)
start_menu_image = load_image('main_menu.jpg')
start_window.image = start_menu_image

score_window = UIWindow(
    rect=pygame.Rect(
        (-border, -border),
        (screen_width + 2 * border, screen_height + 2 * border)),
    manager=gui_manager,
    visible=False,
)
back_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 460), (130, 50)),
    text='to main menu',
    manager=gui_manager,
    container=score_window,
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