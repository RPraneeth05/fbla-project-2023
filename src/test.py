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

# Quit pygame
pygame.quit()
