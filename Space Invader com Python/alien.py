import pygame


class Alien(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("Sprites/AlienA.fw.png")
        self.image = pygame.transform.scale(self.image, [65, 40])
        self.rect = pygame.Rect(0, 0, 65, 40)

    def check_collision(self, sprite1, sprite2):
        col = pygame.sprite.spritecollide(sprite1, sprite2, False)
        if col:
            self.kill()