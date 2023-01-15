"""Contain Enemy."""
import pygame

from drawable import DrawWithSprite
from player import BaseMovingCreature
from animation_manager import get_animation_files


class Enemy(DrawWithSprite, BaseMovingCreature):
    """Enemy. Can damage player."""

    ENEMY_SPEED = 5
    ENEMY_JUMP_SPEED = 0
    ENEMY_DAMAGE = 1

    def __init__(self, pos, size, image):
        """Initialize Enemy."""
        self.speed = Enemy.ENEMY_SPEED
        self.jump_speed = Enemy.ENEMY_JUMP_SPEED
        self.gravity = Enemy.BASE_GRAVITY
        self.direction = pygame.math.Vector2(0, 0)
        self.size = size

        self.animations = {'run': []}
        self.download_enemy_asset()
        self.frame_index = 0
        self.animation_speed = 0.23
        self.image = self.animations['run'][self.frame_index]
        self.status = 'run'
        self.face_right = True

        self.direction.x = 1

        super().__init__(pos, size, self.image)

    def download_enemy_asset(self):
        """Download enemy asset."""
        hero_path = 'textures/enemy/'
        for animation in self.animations.keys():
            path_animation = hero_path + animation
            self.animations[animation] = get_animation_files(
                path_animation,
                self.size)

    def animate(self):
        """Animate enemy."""
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        image = animation[int(self.frame_index)]
        if self.face_right:
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)

    def get_direction_x(self):
        """Get enemy x direction."""
        if self.direction.x == 1.0:
            self.face_right = False
        else:
            self.face_right = True

    def update(self, shift_x):
        """Update player position and draw it."""
        self.rect.x += shift_x
        self.get_direction_x()
        self.animate()
