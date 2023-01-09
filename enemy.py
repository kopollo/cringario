import pygame

from drawable import DrawWithSprite
from player import BaseMovingCreature


class Enemy(DrawWithSprite, BaseMovingCreature):
    ENEMY_SPEED = 5
    ENEMY_JUMP_SPEED = 0
    ENEMY_DAMAGE = 1

    def __init__(self, pos, size, image):
        super().__init__(pos, size, image)
        self.speed = Enemy.ENEMY_SPEED
        self.jump_speed = Enemy.ENEMY_JUMP_SPEED
        self.gravity = Enemy.BASE_GRAVITY
        self.direction = pygame.math.Vector2(0, 0)

        self.direction.x = 1

    def update(self, shift_x):
        self.rect.x += shift_x
