

import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("Snake Game")

# FPS
clock = pygame.time.Clock()
fps = 30

# Game variables
snake_size = 10
snake_speed = 20

# Font
font = pygame.font.SysFont(None, 25)

# Function to draw snake
def draw_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_size, snake_size])

# Function to display message
def message(msg, color, x = screen_height/3, y = screen_width/3):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [x,y])

# Game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = screen_width/2
    y1 = screen_height/2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1
    snake_direction = None

    # Random food
    foodx = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message("Tu as perdu R pour recommencer ou Q pour quitter", red)
            message("Score: " + str(snake_length - 1), red, y = screen_width/6, x = screen_height/2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_direction != "right":
                    x1_change = -snake_size
                    y1_change = 0
                    snake_direction = "left"
                elif event.key == pygame.K_RIGHT and snake_direction != "left":
                    x1_change = snake_size
                    y1_change = 0
                    snake_direction = "right"
                elif event.key == pygame.K_UP and snake_direction != "down":
                    y1_change = -snake_size
                    x1_change = 0
                    snake_direction = "up"
                elif event.key == pygame.K_DOWN and snake_direction != "up":
                    y1_change = snake_size
                    x1_change = 0
                    snake_direction = "down"
                elif event.key == pygame.K_ESCAPE:
                    game_over = True

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [foodx, foody, snake_size, snake_size])
        
        message("Score: " + str(snake_length - 1), white, y = screen_width/6, x = screen_height/2)
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_size, snake_list)
        pygame.display.update()

        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()

