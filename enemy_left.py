import random

import pygame
from pygame.math import Vector2

snd_dir = 'media/snd/'                                  # Путь до папки со звуками
img_dir = 'media/img/'                                  # Путь до папки со спрайтами

width = 1366                                            # ширина игрового окна
height = 768                                            # высота игрового окна


# Создаем класс врага слева
class EnemyLeft(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)             # Враг - спрайт

        self.image = pygame.image.load(img_dir + 'enemy_left/1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0                                 # По горизонтали - слева
        self.rect.y = random.randint(0, height)         # По вертикали случайное положение
        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0
        self.speedx = random.randint(1, 5)
        self.speedy = random.randint(-5, 5)
        self.hp = 100

        self.snd_expl = pygame.mixer.Sound(snd_dir + "expl.mp3")
        self.snd_expl.set_volume(0.3)

    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)
        self.angle += rotate_speed
        self.image = pygame.transform.rotate(self.copy, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.rotate(5)
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Респаун при выходе за правую, верхнюю, нижнюю границы
        if self.rect.x > width or self.rect.y > height or self.rect.bottom < 0:
            self.rect.x = width
            self.rect.y = random.randint(0, height)
            self.speedx = random.randint(-5, -1)
            self.speedy = random.randint(-5, 5)
