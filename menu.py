import pygame

def draw_text(screen, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.display.blit(text_surface, (x, y))

def draw_button(screen, text, x, y, width, height):
    pygame.draw.rect(screen.display, (0, 0, 0), (x, y, width, height))
    draw_text(screen, text, 36, x + 10, y + 10)

def check_button_click(pos, x, y, width, height):
    return x < pos[0] < x + width and y < pos[1] < y + height