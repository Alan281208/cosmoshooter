import pygame
from pygame.math import Vector2

snd_dir = 'media/snd/'                                  # Путь до папки со звуками
img_dir = 'media/img/'                                  # Путь до папки со спрайтами

width = 1366                                            # ширина игрового окна
height = 768                                            # высота игрового окна


# Создаем класс пули
class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)             # Пуля - спрайт

        self.image = pygame.image.load(img_dir + 'bullet.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, player.angle)  # поворот пули
        self.rect.center = Vector2(player.rect.center)
        self.speed = 30
        self.move = self.speed * player.direction

    def update(self):
        self.rect.center += self.move
        if self.rect.x > width or self.rect.y > height or self.rect.y < 0 or self.rect.x < 0:
            self.kill()
