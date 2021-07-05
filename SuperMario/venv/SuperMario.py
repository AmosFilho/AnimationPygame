from MarioJumping import *
from MarioRunning import *
from MarioWalking import *
import pygame
import sys

pygame.init()
timer = pygame.time.Clock()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Running")
m_position_x = 250
m_position_y = 314

background = pygame.image.load('mario_background')
bg = pygame.transform.scale(background, (400, 400))
running_sprites = pygame.sprite.Group()
jumping_sprites = pygame.sprite.Group()
walking_sprites = pygame.sprite.Group()
mario_running = MarioRunning(m_position_x, m_position_y+20)
mario_jumping = MarioJumping(m_position_x, m_position_y-20)
mario_walking = MarioWalking(m_position_x, m_position_y+20)

mario_image = pygame.image.load('jumping_1')
mario_idle = pygame.transform.scale(mario_image, (25, 64))

jumping_sprites.add(mario_jumping)
running_sprites.add(mario_running)
walking_sprites.add(mario_walking)

while True:
    timer.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mario_jumping.jumping()
            if event.key == pygame.K_RIGHT:
                mario_running.running()
                # mario_running.rect.topleft = [m_position_x+20, m_position_y+20]
            if event.key == pygame.K_LEFT:
                mario_walking.walking()

    screen.fill((0, 100, 255))
    screen.blit(bg, (0, 0))
    if mario_jumping.is_jumping:
        jumping_sprites.draw(screen)
        jumping_sprites.update(1)
    elif mario_running.is_running:
        running_sprites.draw(screen)
        running_sprites.update(1)
    elif mario_walking.is_walking:
        walking_sprites.draw(screen)
        walking_sprites.update(0.6)
    else:
        screen.blit(mario_idle, (m_position_x,  m_position_y))
    pygame.display.flip()
