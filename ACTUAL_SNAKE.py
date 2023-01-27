import pygame
from random import randrange

WINDOW = 640
TILE_SIZE = 32
difficulty = 0
if difficulty == 1:
    WINDOW = 480
elif difficulty == 2:
    WINDOW = 320
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

def get_random_position(): return [randrange(*RANGE), randrange(*RANGE)]

snake = pygame.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 110

# Load image and create rect for it
food_image = pygame.image.load("s.png")
food_rect = food_image.get_rect()
food_rect.center = get_random_position()

screen = pygame.display.set_mode([WINDOW] * 2)
clock = pygame.time.Clock()
while True:
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
    screen.fill('black')
    self_eating = pygame.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food_rect.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]
    if snake.center == food_rect.center:
        food_rect.center = get_random_position()
        length += 1
    screen.blit(food_image, food_rect)
    [pygame.draw.rect(screen, 'green', segment) for segment in segments]
    time_now = pygame.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    pygame.display.flip()
    clock.tick(60)