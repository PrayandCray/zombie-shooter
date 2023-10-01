import pygame, sys
from player import *

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Zombie Shooter')

player = Player(screen_width / 2 - (188/2), screen_height / 2 - (160/2), 'player.png')
player.rect.move_ip(player.x, player.y)
player_group = pygame.sprite.Group()
player_group.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player_group.draw(screen)

    pygame.display.flip()
    clock.tick(60)