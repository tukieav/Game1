import pygame
import random
from screen import Screen
from background import Background
from player import Player
from enemies import Enemies, LargeEnemy, Boss
from physics import Physics
from weapons import Weapons
from menu import show_game_over_screen

pygame.init()

screen = Screen()
background = Background()
weapon = Weapons(screen, 'basic')
player = Player(screen, weapon)
enemies = Enemies()
large_enemies = LargeEnemy()
boss = Boss()
physics = Physics(player, enemies, large_enemies, boss, weapon)
boss_created = False
last_enemy_time = 0
last_large_enemy_time = 0

clock = pygame.time.Clock()


running = True
last_shot_time = 0

while running:
    clock.tick(60)
    current_time = pygame.time.get_ticks() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill_background()
    background.update_and_draw(screen)

    if current_time - last_enemy_time > random.uniform(0.5, 1.0):
        enemies.create_enemies(screen.window_width)
        last_enemy_time = current_time

    if current_time - last_large_enemy_time > random.uniform(5.0, 10.0):
        large_enemies.create_enemies(screen.window_width)
        last_large_enemy_time = current_time

    if player.points % 200 == 0 and player.points != 0 and not boss_created:
        boss.create_enemies(screen.window_width)
        boss_created = True


    enemies.update_and_draw(screen)
    large_enemies.update_and_draw(screen)
    boss.update_and_draw(screen)

    player.update_and_draw(screen)

    keys = pygame.key.get_pressed()
    shoot_interval = weapon.shoot_interval 
    last_shot_time = player.shoot(keys, current_time, last_shot_time, shoot_interval)

    weapon.update_bullets()
    weapon.draw_bullets(screen)

    physics.check_collisions_and_hits()

    if physics.check_game_over():
        running, player, enemies, physics = show_game_over_screen(
            screen, player, enemies, physics, weapon
        )   

    pygame.display.flip()