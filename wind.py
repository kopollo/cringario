from drawable import DrawWithSprite
from animation_manager import get_animation_files
import pygame
import random


class Wind(DrawWithSprite):
    def __init__(self, pos, size):
        self.step = 80
        self.direction = pygame.math.Vector2(-1, 1)

        self.leafs = pygame.sprite.Group()

        self.animations = {'fall': []}
        self.download_wind_asset()
        self.frame_index = 0
        self.animation_speed = 0.23
        self.image = self.animations['fall'][self.frame_index]
        self.status = 'fall'

    def download_wind_asset(self):
        """Download sakura asset."""
        hero_path = 'textures/wind/'
        for animation in self.animations.keys():
            path_animation = hero_path + animation
            self.animations[animation] = get_animation_files(
                path_animation,
                self.size)

    def animate(self):
        """Animate wind."""
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        image = animation[int(self.frame_index)]
        self.image = image

    def update(self):
        pass


def generate_leafs():
    first_leaf_pos = random.randint(0, 50)
    step = 80

    leafs = pygame.sprite.Group()

    for i in range((1200 * 10)//step):
        leaf = Wind(first_leaf_pos, 10)
        leafs.add(leaf)
        first_leaf_pos += step

    return leafs
