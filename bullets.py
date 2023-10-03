import pygame, math

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

    def shoot(self, screen_width, screen_height):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:

            mouse_x, mouse_y = pygame.mouse.get_pos()
            direction = pygame.math.Vector2(mouse_x - self.pos.x, mouse_y - self.pos.y)
            angle = math.degrees(math.atan2(direction.y, direction.x))

            self.image = pygame.transform.rotate(self.original_image, -angle)
            self.rect = self.image.get_rect(center=self.pos)

            self.x_vel = math.cos(math.radians(angle)) * self.speed
            self.y_vel = math.sin(math.radians(angle)) * self.speed

            self.pos.x += self.x_vel
            self.pos.y += self.y_vel
            self.rect.center = self.pos
            if self.rect.right < 0 or self.rect.left > screen_width or self.rect.bottom < 0 or self.rect.top > screen_height:
                self.kill()