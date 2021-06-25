import pygame
from player import Player
from alien import Alien
from bullet import Bullet

# o Game.
pygame.init()
display = pygame.display.set_mode([840, 680])
pygame.display.set_caption("Space Invaders por Ancarus")

running_game_app = True
clock = pygame.time.Clock()
timer = 0

def draw_display():
    display.fill([0, 0, 0])


# Objects
object_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
player = Player(object_group)

for alien_y in range(5):
    for alien_x in range(11):
        new_alien = Alien(object_group, alien_group)
        new_alien.rect = pygame.Rect(75 * alien_x, 45 * alien_y, 65, 40)


def shooting():
    Bullet.bullet_on_display = True
    new_bullet = Bullet(object_group, bullet_group)
    new_bullet.rect = pygame.Rect(player.rect.centerx - 7, player.rect.centery - 32, 15, 25)


if __name__ == "__main__":
    while running_game_app:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game_app = False

        # UpDate estilo unity

        draw_display()
        object_group.update()
        # Checking collision between Bullet group and Alien Group, If destroy Bullet and Destroy Alien
        collision_alien_x_bullet = pygame.sprite.groupcollide(bullet_group, alien_group, True, True)

        if collision_alien_x_bullet:
            Bullet.bullet_on_display = False

        if pygame.key.get_pressed()[pygame.K_SPACE] and not Bullet.bullet_on_display:
            shooting()

        object_group.draw(display)
        pygame.display.update()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
