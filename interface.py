
import pygame

def draw_points(screen, points):
    font = pygame.font.Font(None, 36)
    text = font.render(f'Points: {points}', True, (255, 255, 255))
    screen.display.blit(text, (10, 10))

def draw_health(screen, health):
    font = pygame.font.Font(None, 36)
    text = font.render(f'HP: {health}', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topright = (screen.window_width - 10, 10)
    screen.display.blit(text, text_rect)