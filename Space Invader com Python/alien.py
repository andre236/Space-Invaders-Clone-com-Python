import pygame


class Alien(pygame.sprite.Sprite):
    moving_right = True
    approaching_player = False

    def __init__(self, *groups, alien_type):
        super().__init__(*groups)
        if alien_type == "a":
            self.image = pygame.image.load("Sprites/AlienA.fw.png")
            self.image = pygame.transform.scale(self.image, [32, 32])
            self.rect = pygame.Rect(0, 0, 32, 32)
        elif alien_type == "b":
            self.image = pygame.image.load("Sprites/AlienB.png")
            self.image = pygame.transform.scale(self.image, [52, 32])
            self.rect = pygame.Rect(0, 0, 52, 32)
        elif alien_type == "c":
            self.image = pygame.image.load("Sprites/AlienC.fw.png")
            self.image = pygame.transform.scale(self.image, [52, 32])
            self.rect = pygame.Rect(0, 0, 52, 32)

        self.speed = 1

    def update(self, *args, **kwargs) -> None:
        if Alien.moving_right:
            self.rect.x += self.speed
        elif not Alien.moving_right:
            self.rect.x -= self.speed

        if Alien.approaching_player:
            self.rect.y += 5