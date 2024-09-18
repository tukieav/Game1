import pygame

class Screen:
    def __init__(self):
        self.window_width = 768  # Przykładowa szerokość
        self.window_height = 512  # Przykładowa wysokość
        self.display = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('Star Killer')
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.RED = (255, 0, 0)
        self.SPACE = (32, 54, 88)

    def fill_background(self):
        self.display.fill(self.SPACE)