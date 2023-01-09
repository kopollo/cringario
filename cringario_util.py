import os
import sys

import pygame
import yaml


def read_config():
    with open('config.yml', 'r') as f:
        return yaml.safe_load(f)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    return image


def terminate():
    pygame.quit()
    sys.exit()
