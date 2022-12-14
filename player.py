import pygame
from abc import abstractmethod, ABC
from drawable import DrawWithSprite
from cringario_util import load_image

JUMP_POWER = 10
GRAVITY = 0.35


class BaseAliveCreature(ABC):
    def __init__(self, x, y):
        pass

    @abstractmethod
    def player_move(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get_damage(self):
        pass

    @abstractmethod
    def make_hit(self):
        pass

    @abstractmethod
    def set_dead(self):
        pass


class Hero(DrawWithSprite):
    image = load_image("bomb.png")

    def __init__(self, pos, size):
        super().__init__(pos, size, Hero.image)
        self.speed = 9
        self.jump_speed = -13
        self.gravity = 0.6
        self.direction = pygame.math.Vector2(0, 0)

    def player_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def jump(self):
        self.direction.y = self.jump_speed

    def gravity_work(self):
        self.direction.y += self.gravity

    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.player_move()
        self.gravity_work()
