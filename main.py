import pygame
import random
import screen

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
shoot_interval = 0.1

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
        draw_text(screen, "You Loose! Restart?", 64, screen.window_width // 4, screen.window_height // 4)
        draw_button(screen, "Yes", screen.window_width // 2 - 60, screen.window_height // 2 - 50, 100, 50)
        draw_button(screen, "No", screen.window_width // 2 + 60, screen.window_height // 2 - 50, 100, 50)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if check_button_click(pos, screen.window_width // 2 - 60, screen.window_height // 2 - 50, 100, 50):
                        player = Player(screen, weapon)
                        enemies = Enemies()
                        physics = Physics(player, enemies, weapon, weapon)
                        waiting = False
                    elif check_button_click(pos, screen.window_width // 2 + 60, screen.window_height // 2 - 50, 100, 50):
                        running = False
                        waiting = False

    pygame.display.flip()