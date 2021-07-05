import pygame


class MarioRunning(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_running = False
        self.sprites.append(pygame.image.load('running_1'))
        self.sprites.append(pygame.image.load('running_2'))
        self.sprites.append(pygame.image.load('running_3'))
        for i in range(len(self.sprites)):
            self.sprites[i] = pygame.transform.scale(self.sprites[i], (23, 29))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y+15]

    def running(self):
        self.is_running = True

    def update(self, speed):
        if self.is_running:
            self.current_sprite += speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_running = False
            self.image = self.sprites[int(self.current_sprite)]
