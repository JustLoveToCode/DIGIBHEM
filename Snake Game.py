import pygame
import random

# Initialize Pygame
pygame.init()

# Set the Display or Size of the Screen
# Declaring the screen_width and the screen_height Variable here:
screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
# Caption to be displayed on the screen:
pygame.display.set_caption("Snake Game with Obstacles")

# Generating random coordinate for the food
food = 10
# Ensuring Food is generated within the Screen:
foodie_x = random.randint(3, screen_width - 25)
foodie_y = random.randint(3, screen_height - 25)

# Setting the Starting Coordinate of the Rectangle using the
# Starting point for the x and y coordinate:
x = 150
y = 130

# Setting the Change in the x and y:
x_change = 0
y_change = 0

# Setting the Color Globally here:
cyan = (0, 100, 100)
white = (255, 255, 255)
orange = (255, 191, 0)
green = (0, 255, 0)
black = (0, 0, 0)
pink = (255, 192, 203)


# Define the set_random_color() function:
def set_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Defining Snake Movement:
snake_movement = 5


# Setting the initial Length of the Snake:
snake_length = 1

# List to Store the Segment of the Snake
snake_segments = []

# Setting the Collision Radius:
collision_radius = 12

# Setting the Initial Score:
score = 0

# Defining the message and how it is displayed:
def message(msg, color):
    font = pygame.font.SysFont('Arial', 30)
    text_surface = font.render(msg, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (screen_width / 2, screen_height / 2)
    screen.blit(text_surface, text_rect)


# Display the Score in the Scoreboard:
def display_score():
    font = pygame.font.SysFont('Arial', 40)
    score_text = font.render("Score " + str(score), True, white)
    screen.blit(score_text, (20, 20))

# List to Store the Obstacles Coordinate:
obstacles = []


# Coordinate to generate the Obstacles
def generate_obstacle():
    obstacles.clear()
    obstacle_x = random.randint(0, screen_width - 15)
    obstacle_y = random.randint(0, screen_height - 15)
    obstacles.append((obstacle_x, obstacle_y))

# Draw the Obstacle
def draw_obstacles():
    # Looping through the List for the obstacles:
    for obstacle in obstacles:
        obstacle_x, obstacle_y = obstacle
        # Obstacles in the form of black circle:
        pygame.draw.circle(screen, black, (obstacle_x + 7, obstacle_y + 7), 7)


# Game Loop
game_over = False

clock = pygame.time.Clock()

# While not Game Over:
while not game_over:
    # Different events in the pygame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_movement
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_movement
                y_change = 0
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = snake_movement
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -snake_movement
    # Movement of the x and y of the snake:
    x += x_change
    y += y_change
    # The background color to be filled:
    screen.fill(cyan)

    # Drawing the Snake Body Segment
    snake_head = [x, y]
    snake_segments.append(snake_head)
    # Checking the length of the snake to see if it is larger than snake_length
    if len(snake_segments) > snake_length:
        # Delete the older snake_segment
        del snake_segments[0]
    # Invoking the function for draw_obstacles:
    draw_obstacles()

    # Draw the snake segments:
    for segment in snake_segments:
        pygame.draw.rect(screen, pink, [segment[0], segment[1], 15, 15])


    # The starting point of the head of the snake
    pygame.draw.rect(screen, white, [x, y, 15, 15])
    
    if abs(x - foodie_x) < collision_radius and abs(y - foodie_y) < collision_radius:
        foodie_x = random.randint(3, screen_width - 25)
        foodie_y = random.randint(3, screen_height - 25)
        snake_length += 1
        score += 1
        # Invoking the function for generate_obstacle()
        generate_obstacle()
    # Defining the Game Over Criteria:
    # Additional: If the snake collide with the Black Obstacles:
    if any(abs(x - obstacle_x) < collision_radius and abs(y - obstacle_y) < collision_radius for obstacle_x, obstacle_y in obstacles):
        game_over = True
    # If the snake collide with the Screen Boundary:
    if x >= screen_width or x < 0 or y >= screen_height or y < 0:
        game_over = True

    # If the snake collide with its own body:
    if snake_segments.count(snake_head) > 1:
        game_over = True

    # Display Game Over Message:
    if game_over:
        message(f"Game Over: Score {score}", orange)
        pygame.display.update()
        pygame.time.delay(3000)

    # Draw the food for the snake:
    pygame.draw.rect(screen, set_random_color(), [foodie_x, foodie_y, 15, 15])
    
    # Invoking the display_score() function:
    display_score()
    # Using pygame.display.update() to update the display accordingly:
    pygame.display.update()
    # How fast the game will run:
    clock.tick(30)
# Quit the pygame:
pygame.quit()
quit()
