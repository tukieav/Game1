import pygame

from screen import Screen


class Player:
    def __init__(self, screen):
        self.screen = screen
        self.size = 10
        self.player_x = screen.window_width // 2 - self.size // 2
        self.player_y = screen.window_height - self.size - 10
        self.speed = 0.5

    def move_player(self, keys):
        if keys[pygame.K_LEFT] and self.player_x > 0:
            self.player_x -= self.speed
        if keys[pygame.K_RIGHT] and self.player_x < self.screen.window_width - self.size:
            self.player_x += self.speed

    def draw_player(self, screen):
        pygame.draw.rect(screen.display, screen.YELLOW, (self.player_x, self.player_y, self.size, self.size))