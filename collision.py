"""Contain Collision."""
import pygame


class Collision:
    """Class that adds collision ability to BaseMovingCreature."""

    def __init__(self, target_group, platforms: pygame.sprite.Group):
        """
        Initialize collision.

        :param target_group: sprite group we wanted to add collision
        :param platforms: sprite group of objects with whom will be collision
        """
        self.target_group = target_group
        self.platforms = platforms

    def horizontal_movement_collision(self):
        """Implement horizontal movement collision."""
        for target in self.target_group:
            target.move_x()
            for sprite in self.platforms.sprites():
                if sprite.rect.colliderect(target.rect):
                    if target.direction.x < 0:
                        target.rect.left = sprite.rect.right
                        target.direction.x = 1
                    elif target.direction.x > 0:
                        target.rect.right = sprite.rect.left
                        target.direction.x = -1

    def vertical_movement_collision(self):
        """Implement vertical movement collision."""
        for target in self.target_group:
            target.gravity_work()
            for sprite in self.platforms.sprites():
                if sprite.rect.colliderect(target.rect):
                    if target.direction.y > 0:
                        target.rect.bottom = sprite.rect.top
                        target.direction.y = 0
                        target.in_air = False
                    elif target.direction.y < 0:
                        target.rect.top = sprite.rect.bottom
                        target.direction.y = 0

    def apply(self):
        """Call movement collision functions."""
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
