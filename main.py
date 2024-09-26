import pygame
import random
import screen
import menu

from player import Player
from screen import Screen
from background import Background
from enemies import Enemies
from physics import Physics
from weapons import Weapons
from menu import draw_text, draw_button, check_button_click

pygame.init()

screen = Screen()
weapon = Weapons(screen, 'basic')
player = Player(screen, weapon)
background = Background()
enemies = Enemies()
physics = Physics(player, enemies, weapon, weapon)

running = True
last_shot_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill_background()

    if random.randint(0, 20) < 1:
        background.create_stars(screen.window_width)

    background.update_stars(screen.window_height)
    background.draw_stars(screen)

    if random.randint(0, 1000) < 1:
        enemies.create_enemies(screen.window_width)

    enemies.update_enemies(screen.window_height)
    enemies.draw_enemies(screen)

    player.draw_player(screen)

    keys = pygame.key.get_pressed()
    player.move_player(keys)

    current_time = pygame.time.get_ticks() / 1000
    player_x, player_y = player.get_position()
    last_shot_time = weapon.shoot_with_interval(keys, current_time, last_shot_time, player_x, player_y)

    weapon.update_bullets()
    weapon.draw_bullets(screen)

    physics.hit_by_bullet(enemies.enemy_list, weapon)

    if physics.check_collisions(player, enemies.enemy_list):
        running, player, enemies, physics = menu.show_game_over_screen(
            screen, draw_text, draw_button, check_button_click, player, enemies, physics, weapon
        )

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill_background()

    if random.randint(0, 20) < 1:
        background.create_stars(screen.window_width)

    background.update_stars(screen.window_height)
    background.draw_stars(screen)

    if random.randint(0, 1000) < 1:
        enemies.create_enemies(screen.window_width)

    enemies.update_enemies(screen.window_height)
    enemies.draw_enemies(screen)

    player.draw_player(screen)

    keys = pygame.key.get_pressed()
    player.move_player(keys)

    current_time = pygame.time.get_ticks() / 1000
    player_x, player_y = player.get_position()
    last_shot_time = weapon.shoot_with_interval(keys, current_time, last_shot_time, player_x, player_y)

    weapon.update_bullets()
    weapon.draw_bullets(screen)

    physics.hit_by_bullet(enemies.enemy_list, weapon)

    if physics.check_collisions(player, enemies.enemy_list):
        running, player, enemies, physics = menu.show_game_over_screen(
    screen, draw_text, draw_button, check_button_click, player, enemies, physics, weapon
)

    pygame.display.flip()