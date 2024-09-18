import pygame
import random
import screen

from player import Player
from screen import Screen
from background import Background
from enemies import Enemies
from physics import Physics

# Inicjalizacja Pygame
pygame.init()

# Inicjalizacja obiektów
screen = Screen()
player = Player(screen)
background = Background()
enemies = Enemies()

# Główna pętla gry
running = True
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

    # Sprawdzanie kolizji
    if Physics.check_collisions(player.player_x, enemies.enemy_list):
        print("Kolizja! Gra zakończona!")
        running = False


    # Odświeżanie ekranu
    pygame.display.flip()