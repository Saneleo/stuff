import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set the window size
screen = pygame.display.set_mode((800, 600))

# Countdown timer
pygame.display.set_caption("Countdown Timer")

# Set the window title
pygame.display.set_caption("Moving Dot with Text")

# Create the moving dot
dot_color = (10, 10, 110)
dot_size = 40
dot = pygame.Surface((dot_size, dot_size))
dot.fill(dot_color)
dot_rect = dot.get_rect()

# Create a list to store the stationary dots
stationary_dots = []

# Set the initial position of the moving dot
dot_rect.x = 400
dot_rect.y = 400

# Define the speed of the moving dot
dot_speed = 3

# Create the stationary dot
stationary_dot_color = (120, 42, 30)
stationary_dot_size = 20
stationary_dot = pygame.Surface((stationary_dot_size, stationary_dot_size))
stationary_dot.fill(stationary_dot_color)
stationary_dot_rect = stationary_dot.get_rect()

# Set the position of the stationary dot
stationary_dot_rect.x = 200
stationary_dot_rect.y = 400

# Create the font
font = pygame.font.Font(None, 36)

# Set the text color
text_color = (0, 0, 0)

# Innitial Countdown
time_left = 30

# Start timer
start_time = time.time()

# Initialize the score
score = 0

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for arrow key events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        dot_rect.y -= dot_speed
    if keys[pygame.K_DOWN]:
        dot_rect.y += dot_speed
    if keys[pygame.K_LEFT]:
        dot_rect.x -= dot_speed
    if keys[pygame.K_RIGHT]:
        dot_rect.x += dot_speed

    # Keep the dot inside the boundary
    if dot_rect.x < 0:
        dot_rect.x = 0
    if dot_rect.y < 0:
        dot_rect.y = 0
    if dot_rect.x > screen.get_width() - dot_size:
        dot_rect.x = screen.get_width() - dot_size
    if dot_rect.y > screen.get_height() - dot_size:
        dot_rect.y = screen.get_height() - dot_size

# Check if the moving dot is close to the stationary dot
    if dot_rect.colliderect(stationary_dot_rect):
        score += 1
        stationary_dot_rect.x = -100
        stationary_dot_rect.y = -100
        time.sleep(.01)
        stationary_dot_rect.x = random.randint(0, screen.get_width() - stationary_dot_size)
        stationary_dot_rect.y = random.randint(0, screen.get_height() - stationary_dot_size)

    # Render the score as text
    score_text = font.render("Score: " + str(score), True, text_color)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (screen.get_width() // 2, 50)

    # Fill the screen with a color
    screen.fill((200, 200, 200))

    # Draw the stationary dot
    screen.blit(stationary_dot, stationary_dot_rect)

    # Draw the moving dot
    screen.blit(dot, dot_rect)

    # Draw the score text on the screen
    screen.blit(score_text, score_text_rect)

    # Calculate the time elapsed
    elapsed_time = int(time.time() - start_time)

    # Calculate the time left
    time_left = 30 - elapsed_time

    # If the time is up, end the game
    if time_left <= 0:
        running = False

    # Render the time left as text
    time_left_text = font.render("Time left: " + str(time_left), True, text_color)
    time_left_text_rect = time_left_text.get_rect()
    time_left_text_rect.center = (screen.get_width() // 2, 50)
    time_left_text_rect.x = 10
    time_left_text_rect.y = 10

    # Draw the time left text on the screen
    screen.blit(time_left_text, time_left_text_rect)

    # Render the time left as text
    time_left_text = font.render("Time left: " + str(time_left), True, text_color)
    time_left_text_rect = time_left_text.get_rect()
    time_left_text_rect.topleft = (10, 10)  # Change the position to the top left

    # Check if the time is up
    if time_left <= 0:
        # Render the final score text
        final_score_text = font.render("Final score: " + str(score), True, text_color)
        final_score_text_rect = final_score_text.get_rect()
        final_score_text_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        screen.blit(final_score_text, final_score_text_rect)
        pygame.display.update()
        time.sleep(5)

        # Stop the game loop
        running = False

    # Draw the time left text on the screen
    screen.blit(time_left_text, time_left_text_rect)

    # Update the screen
    pygame.display.update()
    # Pause for 5 seconds
pygame.quit()
