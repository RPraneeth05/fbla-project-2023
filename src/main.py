import pygame
import sys

background_color = 0, 0, 0

screen_size = width, height = 500, 500
screen = pygame.display.set_mode(screen_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(background_color)
    pygame.display.flip()