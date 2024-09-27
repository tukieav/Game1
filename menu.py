import pygame
from player import Player
from enemies import Enemies
from physics import Physics

def draw_text(screen, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.display.blit(text_surface, (x, y))

def draw_button(screen, text, x, y, width, height):
    pygame.draw.rect(screen.display, (0, 0, 0), (x, y, width, height))
    draw_text(screen, text, 36, x + 10, y + 10)

def check_button_click(pos, x, y, width, height):
    return x < pos[0] < x + width and y < pos[1] < y + height

def show_game_over_screen(screen, draw_text, draw_button, check_button_click, player, enemies, physics, weapon):
    draw_text(screen, "You Loose! Restart?", 64, screen.window_width // 4, screen.window_height // 4)
    draw_button(screen, "Yes", screen.window_width // 2 - 60, screen.window_height // 2 - 50, 100, 50)
    draw_button(screen, "No", screen.window_width // 2 + 60, screen.window_height // 2 - 50, 100, 50)
    draw_text(screen, "Punkty = " + str(player.points), 64, screen.window_width // 2, screen.window_height // 2)
    pygame.display.flip()

    waiting = True
    running = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                waiting = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if check_button_click(pos, screen.window_width // 2 - 60, screen.window_height // 2 - 50, 100, 50):
                    player = Player(screen, weapon)
                    enemies = Enemies()
                    physics = Physics(player, enemies, weapon, weapon)
                    waiting = False
                elif check_button_click(pos, screen.window_width // 2 + 60, screen.window_height // 2 - 50, 100, 50):
                    running = False
                    waiting = False
    return running, player, enemies, physics

