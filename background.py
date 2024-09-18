import random
import pygame
from screen import Screen

class Background:
    def __init__(self):
        self.star_size = 1
        self.star_speed = 1
        self.star_list = []

    def create_stars(self, window_width):
        x_pos = random.randint(0, window_width - self.star_size)
        self.star_list.append([x_pos, 0])

    def draw_stars(self, screen):
        for star in self.star_list:
            pygame.draw.rect(screen.display, screen.YELLOW, (star[0], star[1], self.star_size, self.star_size))
    
    def update_stars(self, window_height):
        self.star_list = [star for star in self.star_list if star[1] < window_height]
        for star in self.star_list:
            star[1] += self.star_speed