import pygame


class Bullet(pygame.sprite.Sprite):
    bullet_on_display = False

    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load("Sprites/bulletPlayer.fw.png")
        self.image = pygame.transform.scale(self.image, [5, 25])
        self.speed = 10
        self.rect = self.image.get_rect()

    def update(self, *args, **kwargs) -> None:
        self.rect.y -= self.speed

        if self.rect.top < 0:
            Bullet.bullet_on_display = False
            self.kill()
