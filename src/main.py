# Import statements
import pygame
from random import randrange

# Window variables
WINDOW = 640
TILE_SIZE = 32
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)


def get_random_position(): return [randrange(*RANGE), randrange(*RANGE)]


# Snake definition
snake = pygame.rect.Rect([0, 0, TILE_SIZE, TILE_SIZE])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)

# Time control
time, time_step = 0, 100

# Food definition
food = snake.copy()
food.center = get_random_position()

# Pygame initialization
screen = pygame.display.set_mode([WINDOW] * 2)
clock = pygame.time.Clock()

# Event loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake_dir = (0, -TILE_SIZE)
            if event.key == pygame.K_a:
                snake_dir = (-TILE_SIZE, 0)
            if event.key == pygame.K_s:
                snake_dir = (0, TILE_SIZE)
            if event.key == pygame.K_d:
                snake_dir = (TILE_SIZE, 0)

    # Fill screen
    screen.fill('black')

    # Wall collisions and eating self
    self_eating = pygame.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]

    # Check food
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1

    # Draw food
    pygame.draw.rect(screen, 'red', food)

    # Draw snake
    [pygame.draw.rect(screen, 'green', segment) for segment in segments]

    # Move snake
    time_now = pygame.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    # Enable display
    pygame.display.flip()
    clock.tick(60)
