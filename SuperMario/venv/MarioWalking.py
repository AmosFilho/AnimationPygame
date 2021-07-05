import pygame


class MarioWalking(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_walking = False
        self.sprites.append(pygame.image.load('walking-1'))
        self.sprites.append(pygame.image.load('walking-2'))
        self.sprites.append(pygame.image.load('walking-3'))
        self.sprites.append(pygame.image.load('walking-4'))
        self.sprites.append(pygame.image.load('walking-5'))
        self.sprites.append(pygame.image.load('walking-6'))
        for i in range(len(self.sprites)):
            self.sprites[i] = pygame.transform.scale(self.sprites[i], (23, 29))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y+15]

    def walking(self):
        self.is_walking = True

    def update(self, speed):
        if self.is_walking:
            self.current_sprite += speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_walking = False
            self.image = self.sprites[int(self.current_sprite)]
