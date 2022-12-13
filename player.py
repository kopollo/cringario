import pygame
from abc import abstractmethod, ABC

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

    @abstractmethod
    def get_damage(self):
        pass

    @abstractmethod
    def make_hit(self):
        pass

    @abstractmethod
    def set_dead(self):
        pass


class Hero(BaseAliveCreature):
    def __init__(self, x, y):
        self.startX = x  # Начальная позиция Х
        self.startY = y
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.jump_speed = -13
        self.gravity = 0.6


    def player_move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x += 1

        if keys[pygame.K_LEFT]:
            self.direction.x -= 1

        else:
            self.direction.x = 0

    def jump(self):
        self.direction.y = self.jump_speed

    def gravity_work(self):
        self.direction.y += self.gravity

    def update(self):
        self.player_move()
        self.gravity_work()
        return (self.direction.x * self.speed, self.direction.y)

