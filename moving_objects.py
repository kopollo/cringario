import pygame
from abc import abstractmethod, ABC
from drawable import DrawWithSprite
from cringario_util import load_image


class BaseMovingCreature(ABC):
    BASE_SPEED = 8
    BASE_JUMP_SPEED = -15
    BASE_GRAVITY = 0.3

    def __init__(self):
        self.speed = self.BASE_SPEED
        self.jump_speed = self.BASE_JUMP_SPEED
        self.gravity = self.BASE_GRAVITY
        self.direction = pygame.math.Vector2(0, 0)

        self.direction.x = 1
        self.is_corner = False

    def move_x(self):
        self.rect.x += self.direction.x * self.speed

    def jump(self):
        self.direction.y = self.jump_speed

    def gravity_work(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    @abstractmethod
    def update(self):
        pass


class Hero(DrawWithSprite, BaseMovingCreature):
    image = load_image("frog.png")
    HERO_HEALTH = 3

    def __init__(self, pos, size):
        super().__init__(pos, size, Hero.image)
        self.speed = Hero.BASE_SPEED
        self.jump_speed = Hero.BASE_JUMP_SPEED
        self.gravity = Hero.BASE_GRAVITY
        self.direction = pygame.math.Vector2(0, 0)

        self.score = 0
        self.hp = Hero.HERO_HEALTH
        self.in_air = True

    def keyboard_checker(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_w] and not self.in_air:
            self.jump()
            self.in_air = True

    def add_score(self, score):
        self.score += score

    def add_hp(self, hp):
        self.hp += hp

    def update(self):
        self.keyboard_checker()


class Enemy(DrawWithSprite, BaseMovingCreature):
    image = load_image("bad.png")
    ENEMY_SPEED = 5
    ENEMY_JUMP_SPEED = 0

    def __init__(self, pos, size):
        super().__init__(pos, size, Enemy.image)
        self.speed = Enemy.ENEMY_SPEED
        self.jump_speed = Enemy.ENEMY_JUMP_SPEED
        self.gravity = Enemy.BASE_GRAVITY
        self.direction = pygame.math.Vector2(0, 0)

        self.direction.x = 1

    def update(self, shift_x):
        self.rect.x += shift_x
