import pygame, sys
from player import *
from crosshair import *

def callfunc():
    screen.fill(bg_color)
    crosshair.update()
    player.mousepoint()
    player_group.draw(screen)
    crosshair_group.draw(screen)

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Zombie Shooter')
pygame.mouse.set_visible(False)
bg_color = pygame.Color('grey12')

player = Player(screen_width / 2, screen_height / 2 - 50, 'player.png')
player_group = pygame.sprite.Group()
player_group.add(player)

crosshair = Crosshair(screen_width / 2, screen_height / 2 - 50, 'zombie_crosshair.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    callfunc()

    pygame.display.flip()
    clock.tick(60)