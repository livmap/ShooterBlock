import pygame
import sys

# Initialize pygame
pygame.init()

# Window settings
WIDTH = 800
HEIGHT = 600

# Create the window

background = (30, 30, 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ShooterBlock")

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Fill the screen with a color
    screen.fill(background)
    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()