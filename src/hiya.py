import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
x,y = screen.get_size()

screen.fill((255, 255, 255))

pygame.draw.rect(screen, (0, 0, 255), (50, 20, 700, 250))

pygame.draw.rect(screen, (0, 255, 0), (x/2-300 + 25, 290, 175, 130))
pygame.draw.rect(screen, (0, 255, 0), (x/2-300 + 25, 460, 175, 130))

pygame.draw.rect(screen, (0, 255, 0), (x/2+125 - 25, 290, 175, 130))
pygame.draw.rect(screen, (0, 255, 0), (x/2+125 - 25, 460, 175, 130))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos
        if (x/2-300 + 25 < mouse_pos[0] < x/2-300 + 25 + 175) and (290 < mouse_pos[1] < 290 + 130):
            running = False
        if (x/2-300 + 25 < mouse_pos[0] < x/2-300 + 25 + 175) and (460 < mouse_pos[1] < 460 + 130):
            running = False
        if (x/2+125 - 25 < mouse_pos[0] < x/2+125 - 25 + 175) and (290 < mouse_pos[1] < 290 + 130):
            running = False
        if (x/2+125 - 25 < mouse_pos[0] < x/2+125 - 25 + 175) and (460 < mouse_pos[1] < 460 + 130):
            running = False

# Quit pygame
pygame.quit()
