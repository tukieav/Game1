import random
import pygame
from screen import Screen

class Enemies:
    def __init__(self):
        self.enemy_size = 20
        self.enemy_speed = 2
        self.enemy_health = 1
        self.enemy_list = []
        self.points = 1
        self.damage = 10

    def create_enemies(self, window_width):
        x_pos = random.randint(0, window_width - self.enemy_size)
        enemy = [x_pos, 0, self.enemy_health, self.enemy_size, self.points, self.damage]
        self.enemy_list.append(enemy)

    def draw_enemies(self, screen):
        for enemy in self.enemy_list:
            pygame.draw.rect(screen.display, screen.RED, (enemy[0], enemy[1], self.enemy_size, self.enemy_size))
    
    def update_enemies(self, window_height):
        self.enemy_list = [enemy for enemy in self.enemy_list if enemy[1] < window_height]
        for enemy in self.enemy_list:
            enemy[1] += self.enemy_speed

    def update_and_draw(self, screen):
        self.update_enemies(screen.window_height)
        self.draw_enemies(screen)

class LargeEnemy(Enemies):
    def __init__(self):
        super().__init__()
        self.enemy_size = 60
        self.enemy_speed = 1.3
        self.enemy_health = 20
        self.points = 10
        self.damage = 50

    def create_enemies(self, window_width):
        x_pos = random.randint(0, window_width - self.enemy_size)
        enemy = [x_pos, 0, self.enemy_health, self.enemy_size, self.points, self.damage]
        self.enemy_list.append(enemy)

    def draw_enemies(self, screen):
        for enemy in self.enemy_list:
            pygame.draw.circle(screen.display, screen.GREEN, (enemy[0] + self.enemy_size // 2, enemy[1] + self.enemy_size // 2), self.enemy_size // 2)

    def update_enemies(self, window_height):
        self.enemy_list = [enemy for enemy in self.enemy_list if enemy[1] < window_height]
        for enemy in self.enemy_list:
            enemy[1] += self.enemy_speed

    def update_and_draw(self, screen):
        self.update_enemies(screen.window_height)
        self.draw_enemies(screen)


class Boss(Enemies):
    def __init__(self):
        super().__init__()
        self.enemy_size = 250
        self.enemy_speed = 0.1
        self.enemy_health = 150
        self.points = 100
        self.damage = 100

    def create_enemies(self, window_width):
        x_pos = random.randint(0, window_width - self.enemy_size)
        enemy = [x_pos, 0, self.enemy_health, self.enemy_size, self.points, self.damage]
        self.enemy_list.append(enemy)


    def draw_enemies(self, screen):
        for enemy in self.enemy_list:
            pygame.draw.circle(screen.display, screen.WHITE, (enemy[0] + self.enemy_size // 2, enemy[1] + self.enemy_size // 2), self.enemy_size // 2)

    def update_enemies(self, window_height):
        self.enemy_list = [enemy for enemy in self.enemy_list if enemy[1] < window_height]
        for enemy in self.enemy_list:
            enemy[1] += self.enemy_speed

    def update_and_draw(self, screen):
        self.update_enemies(screen.window_height)
        self.draw_enemies(screen)