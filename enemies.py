import random
import pygame
from screen import Screen

class Enemies:
    def __init__(self):
        self.enemy_size = 20
        self.enemy_speed = 0.05
        self.enemy_list = []

    def create_enemies(self, window_width):
        x_pos = random.randint(0, window_width - self.enemy_size)
        self.enemy_list.append([x_pos, 0])

    def draw_enemies(self, screen):
        for enemy in self.enemy_list:
            pygame.draw.rect(screen.display, screen.RED, (enemy[0], enemy[1], self.enemy_size, self.enemy_size))
    
    def update_enemies(self, window_height):
        self.enemy_list = [enemy for enemy in self.enemy_list if enemy[1] < window_height]
        for enemy in self.enemy_list:
            enemy[1] += self.enemy_speed