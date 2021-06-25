import pygame

from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.width_img = 65
        self.height_img = 30
        self.image = pygame.image.load("Sprites/player.png")
        self.image = pygame.transform.scale(self.image, [self.width_img, self.height_img])
        self.rect = pygame.Rect(25, 600, self.width_img, self.height_img)

        self.moveSpeed = 5

    def update(self, *args):
        on_pressed_key = pygame.key.get_pressed()

        if on_pressed_key[pygame.K_d] or on_pressed_key[pygame.K_RIGHT]:
            self.rect.x += self.moveSpeed
        elif on_pressed_key[pygame.K_a] or on_pressed_key[pygame.K_LEFT]:
            self.rect.x -= self.moveSpeed



