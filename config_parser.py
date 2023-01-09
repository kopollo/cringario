import pygame
from cringario_util import load_image
import yaml

pygame.init()

with open('config.yml', 'r') as f:
    data = yaml.safe_load(f)
level_config = data['level']
platform_size = level_config['platform_size']
screen_width = level_config['screen_width']
screen_height = level_config['screen_height']
player_size = level_config['player_size']
screen_size = level_config['screen_size']

path = data['path']
heal_bonus_image = load_image(path['heal_bonus'])
simple_bonus_image = load_image(path['simple_bonus'])

timer = pygame.time.Clock()
