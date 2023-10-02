import pygame

pygame.init()

class Crosshair(pygame.sprite.Sprite):
    
    def __init__(self, x, y, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.x, self.y = x, y

    def update(self):
        self.rect.center = pygame.mouse.get_pos()