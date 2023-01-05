import pygame
from abc import abstractmethod, ABC
import sys
from drawable import DrawWithSprite
from cringario_util import load_image
from import_folder import import_folder


class BaseMovingCreature(ABC):
    BASE_SPEED = 5
    BASE_JUMP_SPEED = -10
    BASE_GRAVITY = 0.5

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
    HERO_HEALTH = 4

    def __init__(self, pos, size, controller):
        self.speed = Hero.BASE_SPEED
        self.jump_speed = Hero.BASE_JUMP_SPEED
        self.gravity = Hero.BASE_GRAVITY
        self.direction = pygame.math.Vector2(0, 0)

        self.spawn_point = pos
        self.score = 0
        self.hp = Hero.HERO_HEALTH
        self.in_air = True
        self.is_invincible = True
        self.invincible_duration = 500
        self.hurt_time = 0
        self.size = size
        self.controller = controller

        self.animations = {'fall': [], 'idle': [], 'jump': [], 'run': []}
        self.download_hero_asset()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image_hero = self.animations['idle'][self.frame_index]
        self.status = 'idle'
        self.face_right = True
        super().__init__(pos, size, self.image_hero)

    def download_hero_asset(self):
        hero_path = 'textures/Hero/'
        for animation in self.animations.keys():
            path_animation = hero_path + animation
            self.animations[animation] = import_folder(
                path_animation,
                self.size)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.face_right:
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)

    def get_status(self):
        if self.direction.y != 0.5 and self.direction.y != 0.0 and self.direction.y < 0.5:  #if self.direction.y < 1 and self.direction.x != 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def keyboard_checker(self):
        keys = pygame.key.get_pressed()
        controller = self.controller
        if keys[controller['right']]:
            self.direction.x = 1
            self.face_right = True
        elif keys[controller['left']]:
            self.direction.x = -1
            self.face_right = False
        else:
            self.direction.x = 0
        if keys[controller['up']] and not self.in_air:
            self.jump()
            self.in_air = True

    def add_score(self, score):
        self.score += score

    def add_hp(self, hp):
        self.hp += hp

    def relocate_to(self, pos):
        self.rect.topleft = pos

    def is_dead(self):
        if self.hp <= 0:
            return True
        return False

    def get_damaged(self, enemy):
        if not self.is_invincible:
            self.is_invincible = True
            self.hp -= enemy.ENEMY_DAMAGE
            self.hurt_time = pygame.time.get_ticks()
            if not self.is_dead():
                self.jump()

    def invincibility_checker(self):
        if self.is_invincible:
            cur_time = pygame.time.get_ticks()
            if cur_time - self.hurt_time >= self.invincible_duration:
                self.is_invincible = False

    def update(self):
        self.keyboard_checker()
        self.invincibility_checker()
        self.get_status()
        self.animate()
        if self.direction.y >= 1:
            self.in_air = True
