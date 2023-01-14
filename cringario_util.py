"""Contain useful global functions"""
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


def load_level(name):
    fullname = os.path.join('levels', name)
    with open(fullname) as data:
        level_map = data.readlines()
    return level_map


def terminate():
    pygame.quit()
    sys.exit()
