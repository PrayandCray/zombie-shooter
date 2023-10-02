import pygame

pygame.init()

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, picture_path):
        super().__init__()
        self.original_image = pygame.image.load(picture_path)
        self.image = self.original_image
        self.x = x
        self.y = y
        self.speed = 7
        self.pos = pygame.math.Vector2(x, y)
        self.rect = self.image.get_rect()