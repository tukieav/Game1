import pygame

from screen import Screen


class Player:
    def __init__(self, screen, weapon):
        self.screen = screen
        self.size = 10
        self.player_x = screen.window_width // 2 - self.size // 2
        self.player_y = screen.window_height - self.size - 10
        self.speed = 0.5

        self.weapon = weapon

    def move_player(self, keys):
        if keys[pygame.K_LEFT] and self.player_x > 0:
            self.player_x -= self.speed
        if keys[pygame.K_RIGHT] and self.player_x < self.screen.window_width - self.size:
            self.player_x += self.speed

    def draw_player(self, screen):
        pygame.draw.rect(screen.display, screen.YELLOW, (self.player_x, self.player_y, self.size, self.size))

    def shoot(self, keys, current_time, last_shot_time, shoot_interval):
        if keys[pygame.K_SPACE] and current_time - last_shot_time > shoot_interval:
            self.weapon.shoot(self.player_x, self.player_y)
            return current_time  # Zwraca czas ostatniego strzału
        return last_shot_time