import pygame
from screen import Screen

class Weapons:
    def __init__(self, screen, weapon):
        self.size = 5
        self.speed = 5
        self.bullets = []
        self.screen = screen

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