import pygame
from screen import Screen
from player import Player

class Weapons:
    def __init__(self, screen, weapon):
        self.size = 5
        self.speed = 5
        self.bullets = []
        self.screen = screen
        self.shoot_interval = 0.1
        self.fire_power = 1

    def shoot(self, player_x, player_y):
        bullet_x = player_x + self.size // 2
        bullet_y = player_y
        self.bullets.append([bullet_x, bullet_y])

    def update_bullets(self):
        for bullet in self.bullets:
            bullet[1] -= self.speed
        self.bullets = [bullet for bullet in self.bullets if bullet[1] > 0]

    def draw_bullets(self, screen):
        for bullet in self.bullets:
            pygame.draw.rect(screen.display, screen.YELLOW, (bullet[0], bullet[1], self.size, self.size))

    def shoot_with_interval(self, keys, current_time, last_shot_time, player_x, player_y):
        if keys[pygame.K_SPACE] and (current_time - last_shot_time) >= self.shoot_interval:
            self.shoot(player_x, player_y)
            return current_time
        return last_shot_time