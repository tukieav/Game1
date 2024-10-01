import pygame
import random
import screen
import menu
import time
import enemies

from player import Player
from screen import Screen
from background import Background
from enemies import Enemies, LargeEnemy, Boss
from physics import Physics
from weapons import Weapons
from menu import draw_text, draw_button, check_button_click

pygame.init()

screen = Screen()
background = Background()
weapon = Weapons(screen, 'basic')
player = Player(screen, weapon)
physics = Physics(player, enemies, weapon, weapon)
enemies = Enemies()
large_enemies = LargeEnemy()
boss = Boss()
boss_created = False

clock = pygame.time.Clock()


running = True
last_shot_time = 0

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill_background()
    if random.randint(0, 20) < 1:
        background.create_stars(screen.window_width)
    background.update_stars(screen.window_height)
    background.draw_stars(screen)

    if random.randint(0, 45) < 1:
        enemies.create_enemies(screen.window_width)

    if random.randint(0, 300) < 1:
        large_enemies.create_enemies(screen.window_width)

    if player.points % 20 == 0 and player.points != 0 and not boss_created:
        boss.create_enemies(screen.window_width)
        boss_created = True  

    if player.points % 20 != 0:
        boss_created = False

    enemies.update_enemies(screen.window_height)
    enemies.draw_enemies(screen)

    large_enemies.update_enemies(screen.window_height)
    large_enemies.draw_enemies(screen)

    boss.update_enemies(screen.window_height)
    boss.draw_enemies(screen)

    player.draw_player(screen)

    keys = pygame.key.get_pressed()
    player.move_player(keys)

    current_time = pygame.time.get_ticks() / 1000
    player_x, player_y = player.get_position()
    last_shot_time = weapon.shoot_with_interval(keys, current_time, last_shot_time, player_x, player_y)

    weapon.update_bullets()
    weapon.draw_bullets(screen)

    physics.hit_by_bullet(enemies.enemy_list, weapon)
    physics.hit_by_bullet(large_enemies.enemy_list, weapon)
    physics.hit_by_bullet(boss.enemy_list, weapon)



    if physics.check_collisions(player, enemies.enemy_list) or physics.check_collisions(player, large_enemies.enemy_list) or physics.check_collisions(player, boss.enemy_list):
        running, player, enemies, physics = menu.show_game_over_screen(
            screen, draw_text, draw_button, check_button_click, player, enemies, physics, weapon
        )

    pygame.display.flip()