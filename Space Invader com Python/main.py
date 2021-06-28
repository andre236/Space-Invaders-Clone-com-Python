import pygame
import random

from player import Player
from alien import Alien
from bullet import Bullet

# o Game.
pygame.init()


# Variables
running_game_app = True
clock = pygame.time.Clock()
timer = 80
current_timer = timer

def draw_display():
    display = pygame.display.set_mode([840, 680])
    pygame.display.set_caption("Space Invaders por Ancarus")
    display.fill([0, 0, 0])
    return display

# SFXs
shot_sfx = pygame.mixer.Sound("music/SFX/cse_slaser.wav")
alien_dying_sfx = pygame.mixer.Sound("music/SFX/cse_shot_hit.wav")

# Fonts
font_standard = pygame.font.SysFont('Arial', 16, False, False)


# HUD
points = 0
message = f'POINTS: {points}'
format_text = font_standard.render(message, False, (255, 255, 255))

# Objects
object_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
player = Player(object_group)

for aliens_pos_y in range(2):
    for aliens_pos_x in range(10):
        new_alien_a = Alien(object_group, alien_group, alien_type="a")
        new_alien_a.rect = pygame.Rect(75 * aliens_pos_x + 30, 45 * aliens_pos_y, 30, 30)

for aliens_pos_y in range(2):
    for aliens_pos_x in range(10):
        new_alien_b = Alien(object_group, alien_group, alien_type="b")
        new_alien_b.rect = pygame.Rect(75 * aliens_pos_x + 20, 90 + (45 * aliens_pos_y), 30, 30)

for aliens_pos_y in range(2):
    for aliens_pos_x in range(10):
        new_alien_c = Alien(object_group, alien_group, alien_type="c")
        new_alien_c.rect = pygame.Rect(75 * aliens_pos_x + 20, 180 + (45 * aliens_pos_y), 30, 30)

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

        current_timer -= 1
        if current_timer <= 0 and Alien.moving_right:
            current_timer = timer
            change_movement(state_move=False)

        elif current_timer <= 0 and not Alien.moving_right:
            current_timer = timer
            change_movement(state_move=True)

        if current_timer <= 5 and not Alien.approaching_player:
            Alien.approaching_player = True
        else:
            Alien.approaching_player = False

        if collision_alien_x_bullet:
            points += 1
            alien_dying_sfx.play()
            Bullet.bullet_on_display = False

        if pygame.key.get_pressed()[pygame.K_SPACE] and not Bullet.bullet_on_display:
            shooting()

        object_group.draw(draw_display())
        pygame.display.update()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
