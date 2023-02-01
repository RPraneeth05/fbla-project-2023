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
food1 = pygame.image.load('./src/letters/A.png')
food1Rect = food1.get_rect()
food1Rect.center = get_random_position()

food2 = pygame.image.load('./src/letters/B.png')
food2Rect = food2.get_rect()
food2Rect.center = get_random_position()

food3 = pygame.image.load('./src/letters/C.png')
food3Rect = food3.get_rect()
food3Rect.center = get_random_position()

food4 = pygame.image.load('./src/letters/D.png')
food4Rect = food4.get_rect()
food4Rect.center = get_random_position()

food5 = pygame.image.load('./src/letters/E.png')
food5Rect = food5.get_rect()
food5Rect.center = get_random_position()

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
        snake.center, food1.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]

    # Check food
    if snake.center == food1Rect.center:
        food1Rect.center = (-999, -999)
        length += 1

    if snake.center == food2Rect.center:
        food2Rect.center = (-999, -999)
        length += 1

    if snake.center == food3Rect.center:
        food3Rect.center = (-999, -999)
        length += 1

    if snake.center == food4Rect.center:
        food4Rect.center = (-999, -999)
        length += 1

    if snake.center == food5Rect.center:
        food5Rect.center = (-999, -999)
        length += 1

    # Draw food
    # pygame.draw.rect(screen, 'red', food1)
    # pygame.draw.rect(screen, 'red', food2)
    # pygame.draw.rect(screen, 'red', food3)
    # pygame.draw.rect(screen, 'red', food4)
    # pygame.draw.rect(screen, 'red', food5)
    screen.blit(food1, food1Rect)
    screen.blit(food2, food2Rect)
    screen.blit(food3, food3Rect)
    screen.blit(food4, food4Rect)
    screen.blit(food5, food5Rect)

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
