import pygame
import random
import screen

from player import Player
from screen import Screen
from background import Background
from enemies import Enemies
from physics import Physics
from weapons import Weapons

# Inicjalizacja Pygame
pygame.init()

# Inicjalizacja obiektów
screen = Screen()
weapon = Weapons(screen, 'basic')
player = Player(screen, weapon)
background = Background()
enemies = Enemies()
physics = Physics(player, enemies, weapon, weapon)

# Główna pętla gry
running = True
last_shot_time = 0
shoot_interval = 0.1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Wypełnianie tła kolorem
    screen.fill_background()

    # Tworzenie nowych gwiazd w tle
    if random.randint(0, 20) < 1:
        background.create_stars(screen.window_width)

    # Aktualizacja pozycji gwiazd
    background.update_stars(screen.window_height)

    # Rysowanie gwiazd
    background.draw_stars(screen)

    # Tworzenie nowych wrogów
    if random.randint(0, 1000) < 1:
        enemies.create_enemies(screen.window_width)

    # Aktualizacja pozycji wrogów
    enemies.update_enemies(screen.window_height)

    # Rysowanie wrogów
    enemies.draw_enemies(screen)

    # Rysowanie gracza
    player.draw_player(screen)

    # Ruch gracza
    keys = pygame.key.get_pressed()
    player.move_player(keys)

    # Strzelanie
    current_time = pygame.time.get_ticks() / 1000
    last_shot_time = player.shoot(keys, current_time, last_shot_time, shoot_interval)

    # Aktualizacja i rysowanie pocisków
    weapon.update_bullets()
    weapon.draw_bullets(screen)

    # Sprawdzanie trafień pociskami
    physics.hit_by_bullet(enemies.enemy_list, weapon)

    # Sprawdzanie kolizji
    if physics.check_collisions(player, enemies.enemy_list):
        print("Kolizja! Gra zakończona!")
        running = False

    # Odświeżanie ekranu
    pygame.display.flip() 