import pygame

# Initialize pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((600, 600))

# Fill the screen with a background color
# screen.fill((255, 255, 255))

# Set the width and height of each grid cell
cell_width = 50
cell_height = 50

# Draw the horizontal grid lines
for y in range(0, 600, cell_height):
    pygame.draw.line(screen, (0, 50, 0), (0, y), (600, y))

# Draw the vertical grid lines
for x in range(0, 600, cell_width):
    pygame.draw.line(screen, (0, 50, 0), (x, 0), (x, 600))

# Update the display
pygame.display.flip()

# Wait for the user to close the window
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
