import pygame


class Bullet(pygame.sprite.Sprite):
    bullet_on_display = False

    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load("Sprites/bulletPlayer.png")
        self.image = pygame.transform.scale(self.image, [15, 25])
        self.speed = 10
        self.rect = self.image.get_rect()

    def update(self, *args, **kwargs) -> None:
        self.rect.y -= self.speed

        if self.rect.top < 0:
            Bullet.bullet_on_display = False
            self.kill()


    def check_collision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col:
            self.kill()