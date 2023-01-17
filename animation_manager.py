"""Animation manager."""
import os
import pygame


def get_animation_files(path, size):
    """Get animation files."""
    surface_list = []

    for _, __, img_files in os.walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale(image_surf, size)
            surface_list.append(image_surf)

    return surface_list
