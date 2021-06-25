import pygame
import random

from player import Player
from alien import Alien
from bullet import Bullet

# o Game.
pygame.init()
display = pygame.display.set_mode([840, 680])
pygame.display.set_caption("Space Invaders por Ancarus")

running_game_app = True
clock = pygame.time.Clock()
timer = 60

def draw_display():
    display.fill([0, 0, 0])

# SFXs
shot_sfx = pygame.mixer.Sound("music/SFX/cse_slaser.wav")
alien_dying_sfx = pygame.mixer.Sound("music/SFX/cse_shot_hit.wav")

# Fonts
font_standard = pygame.font.SysFont('Arial', 16, False, False)


# HUD
points = 0
message = f'POINTS: {points}'
format_text = font_standard.render(message, False, (255, 255, 255))
# display.blit(format_text, (400, 400))

# Objects
object_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
player = Player(object_group)

for alien_y in range(5):
    for alien_x in range(10):
        new_alien = Alien(object_group, alien_group)
        new_alien.rect = pygame.Rect(75 * alien_x + 20, 45 * alien_y, 30, 30)


def shooting():
    shot_sfx.play()
    Bullet.bullet_on_display = True
    new_bullet = Bullet(object_group, bullet_group)
    new_bullet.rect = pygame.Rect(player.rect.centerx - 7, player.rect.centery - 32, 5, 25)

def change_movement(state_move):
    Alien.approaching_player = True
    Alien.moving_right = state_move


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

        timer -= 1
        if timer <= 0 and Alien.moving_right:
            timer = 60
            change_movement(state_move=False)

        elif timer <= 0 and not Alien.moving_right:
            timer = 60
            change_movement(state_move=True)
        if timer <= 5 and not Alien.approaching_player:
            Alien.approaching_player = True
        else:
            Alien.approaching_player = False

        if collision_alien_x_bullet:
            points += random.randint(1, 5)
            alien_dying_sfx.play()
            Bullet.bullet_on_display = False

        if pygame.key.get_pressed()[pygame.K_SPACE] and not Bullet.bullet_on_display:
            shooting()

        object_group.draw(display)
        pygame.display.update()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
