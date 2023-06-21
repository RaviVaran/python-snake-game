import pygame
import time
import random

pygame.init()

# Window dimensions
width = 800
height = 600

# Colors (RGB)
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake dimensions
snake_block = 10
snake_speed = 10

# Font settings
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# Function to display score on the screen
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], snake_block, snake_block])


# Function to display the game over message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])


# Function to run the game
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = width / 2
    y1 = height / 2

    # Initial movement direction of the snake
    x1_change = 0
    y1_change = 0

    # List to keep track of the snake's body
    snake_list = []
    snake_length = 1

    # Generate initial position for the food
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Main game loop
    while not game_over:

        # Game over logic
        while game_close:
            game_display.fill(black)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            # Check for user input after game over
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Update the position of the snake's head
        x1 += x1_change
        y1 += y1_change

        # Check if the snake hits the boundaries of the window
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        game_display.fill(black)
        pygame.draw.rect(game_display, blue, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if the snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()


# Initialize the game window
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Start the game
game_loop()
