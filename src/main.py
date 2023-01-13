import pygame
import sys

pygame.init()

background_color = (0, 0, 0)

screen_size = width, height = (500, 500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Computer Game & Simulation Programming')

text_color = (255, 255, 255)
button_dark = (100, 100, 100)
button_light = (150, 150, 150)

font = pygame.font.SysFont('lucidaconsole', 35)
text = font.render('quit', True, text_color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                sys.exit()

    screen.fill(background_color)
    mouse = pygame.mouse.get_pos()

    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, button_light, [width / 2, height / 2, 140, 40])
    else:
        pygame.draw.rect(screen, button_dark, [width / 2, height / 2, 140, 40])

    screen.blit(text, (width / 2, height / 2))

    pygame.display.flip()
