"""Contain initialization of all global variables and images"""
import pygame
from cringario_util import load_image, read_config

pygame.init()

data = read_config()
level_config = data['level']
platform_size = level_config['platform_size']
screen_width = level_config['screen_width']
screen_height = level_config['screen_height']
player_size = level_config['player_size']
screen_size = level_config['screen_size']

path = data['level_obj_path']
heal_bonus_image = load_image(path['heal_bonus'])
simple_bonus_image = load_image(path['simple_bonus'])
game_fon = load_image(path['game_fon'])
platform_image = load_image(path['platform'])
enemy_image = load_image(path['enemy'])
win_cup_image = load_image(path['win_cup'])
grass_image = load_image(path['grass'])
dirt_image = load_image(path['dirt'])

timer = pygame.time.Clock()
