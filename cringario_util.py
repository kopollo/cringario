"""Contain useful global functions."""
import os
import sys
import pygame
import yaml


def read_config():
    """Read config in convenient way."""
    with open('config.yml', 'r') as f:
        return yaml.safe_load(f)


def load_image(name):
    """
    Load image in pygame view.

    :param name: name of image
    :return: pygame.image
    """
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    return image


def load_level(name):
    """
    Load level map from file.

    :param name: name of file
    :return: level map
    """
    fullname = os.path.join('levels', name)
    with open(fullname) as data:
        level_map = data.readlines()
    return level_map


def terminate():
    """Stop application."""
    pygame.quit()
    sys.exit()
