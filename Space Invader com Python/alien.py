import pygame


class Alien(pygame.sprite.Sprite):
    moving_right = True
    approaching_player = False

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("Sprites/AlienA.fw.png")
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = pygame.Rect(0, 0, 30, 30)
        self.speed = 1

    def update(self, *args, **kwargs) -> None:
        if Alien.moving_right:
            self.rect.x += self.speed
        elif not Alien.moving_right:
            self.rect.x -= self.speed

        if Alien.approaching_player:
            self.rect.y += 5