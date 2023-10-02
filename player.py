import pygame, math

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, picture_path):
        super().__init__()
        self.original_image = pygame.image.load(picture_path)
        self.image = self.original_image
        self.pos = pygame.math.Vector2(x , y)
        self.rect = self.image.get_rect(center=self.pos)
        
    def mousepoint(self):

        mouse_x, mouse_y = pygame.mouse.get_pos()
        direction = pygame.math.Vector2(mouse_x - self.pos.x, mouse_y - self.pos.y)
        angle = math.degrees(math.atan2(direction.y, direction.x))
        self.image = pygame.transform.rotate(self.original_image, -angle +22)
        self.rect = self.image.get_rect(center=self.pos)