import pygame

snd_dir = 'media/snd/'                                  # Путь до папки со звуками
img_dir = 'media/img/'                                  # Путь до папки со спрайтами

width = 1366                                            # ширина игрового окна
height = 768                                            # высота игрового окна


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_dir + 'explosion/0.png')
        self.rect = self.image.get_rect()
        self.anim_speed = 4
        self.frame = 0
        self.anim = [pygame.transform.scale(
                pygame.image.load(img_dir + f'./explosion/{i}.png'),
            (100, 100)) for i in range(9)]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
    def update(self):
        self.image = self.anim[self.frame // self.anim_speed]
        self.frame += 1
        if self.frame >= self.anim_speed*len(self.anim):
            self.kill()
