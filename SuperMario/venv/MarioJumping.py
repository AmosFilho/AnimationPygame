import pygame


class MarioJumping(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_jumping = False
        self.sprites.append(pygame.image.load('jumping_1'))
        self.sprites.append(pygame.image.load('jumping_2'))
        self.sprites.append(pygame.image.load('jumping_3'))
        self.sprites.append(pygame.image.load('jumping_4'))
        self.sprites.append(pygame.image.load('jumping_5'))
        self.sprites.append(pygame.image.load('jumping_6'))
        self.sprites.append(pygame.image.load('jumping_7'))
        self.sprites.append(pygame.image.load('jumping_8'))
        for i in range(len(self.sprites)):
            self.sprites[i] = pygame.transform.scale(self.sprites[i], (25, 64))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y+20]

    def jumping(self):
        self.is_jumping = True

    def update(self, speed):
        if self.is_jumping:
            self.current_sprite += speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_jumping = False
            self.image = self.sprites[int(self.current_sprite)]
