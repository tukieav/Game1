import random
import pygame
from screen import Screen

class Enemies:
    def __init__(self):
        self.enemy_size = 20
        self.enemy_speed = 0.6
        self.enemy_health = 1
        self.enemy_list = []

    def create_enemies(self, window_width):
        x_pos = random.randint(0, window_width - self.enemy_size)
        self.enemy_list.append([x_pos, 0, self.enemy_health, self.enemy_size])

    def draw_enemies(self, screen):
        for enemy in self.enemy_list:
            pygame.draw.rect(screen.display, screen.RED, (enemy[0], enemy[1], self.enemy_size, self.enemy_size))
    
    def update_enemies(self, window_height):
        self.enemy_list = [enemy for enemy in self.enemy_list if enemy[1] < window_height]
        for enemy in self.enemy_list:
            enemy[1] += self.enemy_speed

class LargeEnemy(Enemies):
    def __init__(self):
        super().__init__()
        self.enemy_size = 60
        self.enemy_speed = 0.3
        self.enemy_health = 20

    def create_enemies(self, window_width):
        x_pos = random.randint(0, window_width - self.enemy_size)
        self.enemy_list.append([x_pos, 0, self.enemy_health, self.enemy_size])

    def draw_enemies(self, screen):
        for enemy in self.enemy_list:
            pygame.draw.circle(screen.display, screen.GREEN, (enemy[0] + self.enemy_size // 2, enemy[1] + self.enemy_size // 2), self.enemy_size // 2)

    def update_enemies(self, window_height):
        self.enemy_list = [enemy for enemy in self.enemy_list if enemy[1] < window_height]
        for enemy in self.enemy_list:
            enemy[1] += self.enemy_speed